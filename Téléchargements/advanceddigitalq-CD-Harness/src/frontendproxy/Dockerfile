# Copyright The OpenTelemetry Authors
# SPDX-License-Identifier: Apache-2.0

<<<<<<< HEAD

FROM envoyproxy/envoy-dev:8c202194ac6a2cb781eb6ce27d924b379b1e787f
=======
FROM envoyproxy/envoy:v1.29-latest
>>>>>>> 1a38e439684c06a3f6744fad2f05b5a10c8c7440
RUN apt-get update && apt-get install -y gettext-base && apt-get clean && rm -rf /var/lib/apt/lists/*

USER envoy
WORKDIR /home/envoy
COPY ./src/frontendproxy/envoy.tmpl.yaml envoy.tmpl.yaml

ENTRYPOINT ["/bin/sh", "-c", "envsubst < envoy.tmpl.yaml > envoy.yaml && envoy -c envoy.yaml;"]
