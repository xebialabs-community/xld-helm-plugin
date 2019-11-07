<#include "/helm/helm.ftl">
${helm} ls --namespace ${deployed.namespace}  ${deployed.name}
