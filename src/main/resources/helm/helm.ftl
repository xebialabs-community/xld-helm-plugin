set -x
<#assign helmCmdLine = ["${deployed.container.home}/helm"]/>
<#if helmclient.debug>
 <#assign helmCmdLine = helmCmdLine + ["--debug"]/>
</#if>

<#if helmclient.kubeContext??>
 <#assign helmCmdLine = helmCmdLine + ["--kube-context ${helmclient.kubeContext}"]/>
</#if>

<#if helmclient.kubeConfig??>
 <#assign helmCmdLine = helmCmdLine + ["--kubeconfig ${helmclient.kubeConfig}"]/>
</#if>
<#if helmclient.helmHost??>
 <#assign helmCmdLine = helmCmdLine + ["--host ${helmclient.helmHost}"]/>
</#if>

<#assign helm=helmCmdLine?join(" ")/>

