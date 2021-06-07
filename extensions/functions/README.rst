OpenCensus Python Azure Functions Extension
===========================================

|pypi|

.. |pypi| image:: https://badge.fury.io/py/opencensus-extension-azure-functions.svg
   :target: https://pypi.org/project/opencensus-extension-azure-functions/

Installation
------------

::

    pip install opencensus-extension-azure-functions

Prerequisites
-------------
Install `azure-functions-core-tools <https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Ccsharp%2Cbash>`_
or Azure Functions `vscode-extension <https://docs.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code?tabs=csharp>`_.

How To Use In Python Functions
------------------------------
1. Use ``func init --python`` or ``VSCode Extensions Blade -> Azure -> Functions -> Create New Project...`` to create a Python function app.

2. Use ``func new -a anonymous -t HttpTrigger -n HttpTrigger`` to create an anonymous Http trigger in your function app. If you're using VSCode,
the project creation wizard will guide you through the same process.

3. Include ``opencensus-extension-azure-functions`` and ``requests`` to your requirements.txt

4. In local.settings.json, add new settings ``"PYTHON_ENABLE_WORKER_DEPENDENCIES": "1"`` and ``"APPLICATIONINSIGHTS_CONNECTION_STRING": "InstrumentationKey=aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"``.
You can acquire your appinsights instrumentation key from your Azure Application Insights resource.

5. Set up a virtual environment for your local development:
    1. Create a virtual environment with ``py -3.7 -m venv .venv`` in Windows or ``python3.7 -m venv .venv`` in Unix-like systems.
    2. Activate the virtual environment with ``.venv\Scripts\Activate.ps1`` in Windows PowerShell or ``source .venv/bin/activate`` in Unix-like systems.

6. Change the HTTP trigger file in ``<project_root>/HttpTrigger/\_\_init\_\_.py`` to enable the OpenCensus tracing integration.

.. code:: python
    import json
    import logging

    from opencensus.extension.azure.functions import OpenCensusExtension
    logger = logging.getLogger('HttpTriggerLogger')

    OpenCensusExtension.configure()

    def main(req, context):
        logger.info('Executing HttpTrigger with OpenCensus extension')

        # You must use context.tracer to create spans
        with context.tracer.span("parent"):
            logger.info('Message from HttpTrigger')

        return json.dumps({
            'method': req.method,
            'ctx_func_name': context.function_name,
            'ctx_func_dir': context.function_directory,
            'ctx_invocation_id': context.invocation_id,
            'ctx_trace_context_Traceparent': context.trace_context.Traceparent,
            'ctx_trace_context_Tracestate': context.trace_context.Tracestate,
        })


7. Run it in your local development environment by ``func host start --verbose`` in Core Tools or ``hitting F5`` in VSCode.
8. You should now be able to check the trace information in your Application Insight -> Investigate -> Application Map.

To use Opencensus Python Extensions in other scenarios,
please visit `our example folder <https://github.com/census-ecosystem/opencensus-python-extensions-azure/tree/main/examples>`_

References
----------

* `OpenCensus Project <https://opencensus.io/>`_
* `OpenCensus Python SDK <https://github.com/census-instrumentation/opencensus-python/>`_
* `Python Worker Extension Interface <https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#python-worker-extensions>`_
* `Author Your First Worker Extension <https://docs.microsoft.com/en-us/azure/azure-functions/author-python-worker-extensions>`_
