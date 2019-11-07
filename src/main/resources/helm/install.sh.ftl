<#include "/helm/helm.ftl">


${helm} install ${deployed.chartName} --namespace ${deployed.namespace}  --name ${deployed.name} --version ${deployed.chartVersion} <#list deployed.configurationFiles as cf> -f  ${cf.getFile().getPath()} </#list>

