#
# Copyright 2020 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import json
from overtherepy import OverthereHostSession
import sys

class HelmRunner:

    def __init__(self,helmclient):
        self.helmclient = helmclient

    def get_helm_command(self):
        helm = '{0}/helm'.format(self.helmclient.home)

        if self.helmclient.kubeContext is not None:
            helm = helm + ' --kube-context {0}'.format(self.helmclient.kubeContext)
        if self.helmclient.kubeConfig is not None:
            helm = helm + ' --kubeconfig {0}'.format(self.helmclient.kubeConfig)
        if self.helmclient.helmHost is not None:
            helm = helm + ' --host {0}'.format(self.helmclient.helmHost)
        if self.helmclient.debug:
            helm = helm + ' --debug'
        
        if self.helmclient.caFile is not None:
            helm = helm + ' --ca-file {0}'.format(self.helmclient.caFile)

        if self.helmclient.username is not None:
            helm = helm + ' --username {0}'.format(self.helmclient.username)
        if self.helmclient.password is not None:
            helm = helm + ' --password {0}'.format(self.helmclient.password)
        return helm


    def command_line(self,session,deployed):
        raise Exception("Not Implemented")


    def preview(self,deployed):
        try:
            session = OverthereHostSession(self.helmclient.host,stream_command_output=False)
            command_line = self.command_line(session,deployed)
            print(command_line)
        finally:
            session.close_conn()

    def execute(self,deployed):
        try:
            session = OverthereHostSession(self.helmclient.host,stream_command_output=False)
            command_line = self.command_line(session,deployed)
            print(command_line)
            uploaded_runner = session.upload_text_content_to_work_dir(command_line,'xldeploy_helm.sh',executable=True)
            print(uploaded_runner.path)
            response = session.execute(command_line,check_success=False)
            print "\n".join(response.stdout)
            print "\n".join(response.stderr)
            rc = response.rc
            if response.rc > 0:
                sys.exit(rc)
        finally:
            session.close_conn()



class HelmInstall(HelmRunner):

    def command_line(self,session,deployed):
        return "{0} install {1}".format(self.get_helm_command(),self.parameters(session,deployed))

    def parameters(self,session,deployed):
        values = {'chartName':deployed.chartName,
                'namespace':deployed.container.namespaceName,
                'name':deployed.name,
                'chartVersion': deployed.chartVersion}

        if int(self.helmclient.version) == 2:
            parameters = "{chartName} --namespace {namespace}  --name {name} --version {chartVersion}".format(**values)
        elif int(self.helmclient.version) == 3:
            parameters = "{name} {chartName} --namespace {namespace} --version {chartVersion}".format(**values)
        else:
            raise Exception("Unknown helm version {0}".format(self.helmclient.version))
        
        for cf in deployed.configurationFiles:
            uploaded_file = session.upload_file_to_work_dir(cf.getFile())
            parameters = parameters +" -f "+uploaded_file.getPath()

        return parameters



class HelmUpgrade(HelmRunner):

    def command_line(self,session,deployed):
        return "{0} upgrade {1}".format(self.get_helm_command(),self.parameters(session,deployed))

    def parameters(self,session,deployed):
        values = {'chartName':deployed.chartName,
                'namespace':deployed.container.namespaceName,
                'name':deployed.name,
                'chartVersion': deployed.chartVersion}

        if int(self.helmclient.version) == 2:
            parameters = "{chartName} --namespace {namespace}  --name {name} --version {chartVersion}".format(**values)
        elif int(self.helmclient.version) == 3:
            parameters = "{name} {chartName} --namespace {namespace} --version {chartVersion}".format(**values)
        else:
            raise Exception("Unknown helm version {0}".format(self.helmclient.version))

        for cf in deployed.configurationFiles:
            uploaded_file = session.upload_file_to_work_dir(cf.getFile())
            parameters = parameters +" -f "+uploaded_file.getPath()

        return parameters




