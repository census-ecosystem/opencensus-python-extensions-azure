# Copyright 2021, OpenCensus Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import logging

import requests
from opencensus.extension.azure.functions import OpenCensusExtension
from opencensus.trace import config_integration

"""
This example uses the `OpenCensusExtension` for Azure Functions, which
allows distributed tracing within an Azure Functions environment. It also
sends the dependency/request telemetry collected to Application Insights.
The Azure trace exporter in `opencensus-ext-azure` is replaced by
`OpenCensusExtension`, so it does not need to be instantiated separately.

This example also uses `opencensus-ext-requests` to trace telemetry sent using
the `requests` library.

Ensure the following lines are defined in your function app's `requirements.txt`
and properly installed:
    opencensus-extension-azure-functions
    opencensus-ext-requests

Ensure the following setting is configured in your Azure Functions app or
local.settings.json:
    "PYTHON_ENABLE_WORKER_EXTENSIONS": "1"
    "APPLICATIONINSIGHTS_CONNECTION_STRING": "InstrumentationKey=aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"

For more information about getting started with Azure Functions, please visit
https://aka.ms/functions-python-vscode

For more information about getting started with `OpenCensus` Python SDK, please visit
https://github.com/census-instrumentation/opencensus-python

The `OpenCensusExtension` uses the same configuration as the Azure exporters
in `OpenCensus`. See https://github.com/census-instrumentation/opencensus-python/
tree/master/contrib/opencensus-ext-azure for more details.
"""

config_integration.trace_integrations(['requests'])

# By default, the connection string defined in `APPLICATIONINSIGHTS_CONNECTION_STRING`
# is used to send trace information.
# You can also configure the endpoint to receive your trace information with
# connection_string='InstrumentationKey=<another appinsights key>'
OpenCensusExtension.configure()

def main(req, context):
    logging.info('Executing HttpTrigger with OpenCensus extension')

    # You must use context.tracer to create spans
    with context.tracer.span("parent"):
        response = requests.get(url='http://example.com')

    return json.dumps({
        'method': req.method,
        'response': response.status_code,
        'ctx_func_name': context.function_name,
        'ctx_func_dir': context.function_directory,
        'ctx_invocation_id': context.invocation_id,
        'ctx_trace_context_Traceparent': context.trace_context.Traceparent,
        'ctx_trace_context_Tracestate': context.trace_context.Tracestate,
    })
