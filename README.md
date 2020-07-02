# XL Deploy Helm Plugin

[![Build Status][xld-helm-plugin-travis-image]][xld-helm-plugin-travis-url]
[![License: MIT][xld-helm-plugin-license-image]][xld-helm-plugin-license-url]
![Github All Releases][xld-helm-plugin-downloads-image]

[xld-helm-plugin-travis-image]: https://travis-ci.org/xebialabs-community/xld-helm-plugin.svg?branch=master
[xld-helm-plugin-travis-url]: https://travis-ci.org/xebialabs-community/xld-helm-plugin
[xld-helm-plugin-license-image]: https://img.shields.io/badge/License-MIT-yellow.svg
[xld-helm-plugin-license-url]: https://opensource.org/licenses/MIT
[xld-helm-plugin-downloads-image]: https://img.shields.io/github/downloads/xebialabs-community/xld-helm-plugin/total.svg

## Preface

This document describes the functionality provided by the XL Deploy Helm plugin 
* Support Helm V3 (default)
* Support Helm V2 
* Tested helm running on Unix machines

## Overview

This plugin will allow to deploy a helm chart using XLD. To run the helm chart you need to have the helm binary installed and connect via ssh using overthere plugin.

## Installation

* requirement xl-deploy-server 9.0.0+
* Copy the [overtherepy jar file](https://github.com/xebialabs-community/overthere-pylib/releases/download/v0.0.4/overtherepy-0.0.4.jar) into the `XL_DEPLOY_SERVER/plugins` directory.

* Copy the latest JAR file from the [releases page](https://github.com/xebialabs-community/xld-helm-plugin/releases) into the `XL_DEPLOY_SERVER/plugins` directory.
* Restart the XL Deploy server.

## Sample Configuration
A sample configuration is available in the project.

```
$xl apply --xl-deploy-url http://localhost:4541 -f xebialabs.yaml 


[1/4] Applying infrastructure.yaml (imported by xebialabs.yaml)
    Created CI Infrastructure/helm-sample/xl-demo-kube/demo-helm
    Created CI Infrastructure/helm-sample/xl-demo-kube
    Created CI Infrastructure/helm-sample/localhost/helmClient
    Created CI Infrastructure/helm-sample/localhost
    Created CI Infrastructure/helm-sample

[2/4] Applying environment.yaml (imported by xebialabs.yaml)
    Created CI Environments/helm-sample/dev.conf
    Created CI Environments/helm-sample/xl-demo-helm
    Created CI Environments/helm-sample

[3/4] Applying application.yaml (imported by xebialabs.yaml)
    Created CI Applications/MyHelmSampleApp/2.0.4/mariadb/config.yaml
    Created CI Applications/MyHelmSampleApp/2.0.4/mariadb/override.yaml
    Created CI Applications/MyHelmSampleApp/2.0.4/mariadb
    Created CI Applications/MyHelmSampleApp/2.0.4
    Created CI Applications/MyHelmSampleApp/2.0.5/mariadb/config.yaml
    Created CI Applications/MyHelmSampleApp/2.0.5/mariadb/override.yaml
    Created CI Applications/MyHelmSampleApp/2.0.5/mariadb
    Created CI Applications/MyHelmSampleApp/2.0.5
    Created CI Applications/MyHelmSampleApp

[4/4] Applying xebialabs.yaml
Done
```
## Features

## References

