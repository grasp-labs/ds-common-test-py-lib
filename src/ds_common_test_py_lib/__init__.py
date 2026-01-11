"""
**File:** ``__init__.py``
**Region:** ``ds-common-test-py-lib``

Description
-----------
A Python package from the ds-common-test-py-lib library.

Example
-------
.. code-block:: python

    from ds_common_test_py_lib import __version__

    print(f"Package version: {__version__}")
"""

from importlib.metadata import version

__version__ = version("ds-common-test-py-lib")

__all__ = ["__version__"]
