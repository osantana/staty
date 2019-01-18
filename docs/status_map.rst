Status Map
----------

You can register a custom HTTP status code in staty's global
status map using the ``@status.register()`` decorator:

.. code-block:: python3

   >>> from staty import status, base
   >>> @status.register
   ... class MyCustomClientError(base.ClientError):
   ...     code = 494
   ...     message = "My Client Error"


You can reference to registered status as an attribute of ``status``
using ``status.HTTP_{CODE}_{CLASS_NAME_IN_CONSTANT_NAME_CASE}``:

.. code-block:: python3

   >>> from staty import status
   >>> status.HTTP_494_MY_CUSTOM_CLIENT_ERROR == 494
   True

You can reference an status code using it code as index:

.. code-block:: python3

   >>> status[494] == status.HTTP_494_MY_CUSTOM_CLIENT_ERROR
   True


Class Reference
~~~~~~~~~~~~~~~

.. autoclass:: staty.status_map.HTTPStatusMap
   :members:
   :undoc-members:
   :show-inheritance:
