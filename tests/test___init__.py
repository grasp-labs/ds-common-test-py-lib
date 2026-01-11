"""
File: test___init__.py
Description: Smoke tests ensuring the package can be imported for coverage.
Region: packages/shared
"""

from __future__ import annotations

import importlib


def test_import_package_and_version_is_string() -> None:
    """
    Verify package import works and version is exposed.

    Returns:
        None.
    """

    pkg = importlib.import_module("ds_common_test_py_lib")

    assert isinstance(pkg.__version__, str)
    assert pkg.__version__ != ""
