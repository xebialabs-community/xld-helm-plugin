<#include "/helm/helm.ftl">
${helm} install ${deployed.chartName} --namespace ${deployed.namespace}  --name ${deployed.name} --version ${deployed.version}
