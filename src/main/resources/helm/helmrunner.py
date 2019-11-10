import json
from overtherepy import OverthereHostSession
import sys


def get_helm_command(helmclient):
    helm = '{0}/helm'.format(helmclient.home)

    if helmclient.kubeContext is not None:
        helm = helm + ' --kube-context {0}'.format(helmclient.kubeContext)
    if helmclient.kubeConfig is not None:
        helm = helm + ' --kubeconfig {0}'.format(helmclient.kubeConfig)
    if helmclient.helmHost is not None:
        helm = helm + ' --host {0}'.format(helmclient.helmHost)
    if helmclient.debug:
        helm = helm + ' --debug'
    return helm


def get_install_parameters(session,deployed):
    values = {'chartName':deployed.chartName,
            'namespace':deployed.namespace,
            'name':deployed.name,
            'chartVersion': deployed.chartVersion}

    parameters = "{chartName} --namespace {namespace}  --name {name} --version {chartVersion}".format(**values)
    for cf in deployed.configurationFiles:
        uploaded_file = session.upload_file_to_work_dir(cf.getFile())
        parameters = parameters +" -f "+uploaded_file.getPath()

    return parameters

def get_upgrade_parameters(session,deployed):
    values = {'chartName':deployed.chartName,
            'namespace':deployed.namespace,
            'name':deployed.name,
            'chartVersion': deployed.chartVersion}

    parameters = "{name} {chartName} --namespace {namespace} --version {chartVersion}".format(**values)
    for cf in deployed.configurationFiles:
        uploaded_file = session.upload_file_to_work_dir(cf.getFile())
        parameters = parameters +" -f "+uploaded_file.getPath()

    return parameters

def get_install_commandline(helmclient,session, deployed):
    command_line = "{0} install {1}".format(get_helm_command(helmclient),get_install_parameters(session,deployed))
    return command_line

def get_upgrade_commandline(helmclient,session, deployed):
    command_line = "{0} upgrade {1}".format(get_helm_command(helmclient),get_upgrade_parameters(session,deployed))
    return command_line

def unknown_commandline(helmclient,session, deployed):
    raise Exception("unknown_commandline !! {0}".format(helmcommand))

try:
    session = OverthereHostSession(helmclient.host,stream_command_output=False)
    #TODO manage streams
    command_lines = {
            'install':get_install_commandline,
            'upgrade':get_upgrade_commandline}
    command_line = command_lines.get(helmcommand, unknown_commandline)(helmclient,session,deployed)
    print command_line
    uploaded_runner = session.upload_text_content_to_work_dir(command_line,'xldeploy_helm.sh',executable=True)
    print uploaded_runner.path
    response = session.execute(command_line,check_success=False)
    print "\n ".join(response.stdout)
    rc = response.rc
    if response.rc > 0:
        sys.exit(rc)
finally:
    session.close_conn()


