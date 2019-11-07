<#include "/helm/helm.ftl">

${helm} upgrade ${deployed.name} ${deployed.chartName} --namespace ${deployed.namespace}  --version ${deployed.chartVersion} <#list deployed.configurationFiles as cf> -f  ${cf.getFile().getPath()} </#list>


