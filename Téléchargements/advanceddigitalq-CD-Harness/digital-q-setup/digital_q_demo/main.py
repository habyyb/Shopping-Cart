#!/usr/bin/env python
from constructs import Construct
from cdk8s import App, Chart, Helm


class MyChart(Chart):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

<<<<<<< HEAD
        otel_demo = Helm(self, "otel-demo",
=======
        otel_demo = Helm(self, "otel-demo-o11y",
>>>>>>> 1a38e439684c06a3f6744fad2f05b5a10c8c7440
                    chart= "open-telemetry/opentelemetry-demo")


app = App()
MyChart(app, "digital-q-demo")

app.synth()