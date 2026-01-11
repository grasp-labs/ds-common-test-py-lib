"""
File: test___init__.py
Description: Smoke tests ensuring the package can be imported for coverage.
Region: packages/shared
"""

from __future__ import annotations

import importlib
import importlib.metadata as importlib_metadata


def test_import_package_and_version_is_string() -> None:
    """
    Verify package import works and version is exposed.

    Returns:
        None.
    """

    pkg = importlib.import_module("ds_common_test_py_lib")

    assert isinstance(pkg.__version__, str)
    assert pkg.__version__ != ""


def test_version_falls_back_when_metadata_missing(monkeypatch) -> None:
    """
    Verify the fallback version is used when distribution metadata is missing.

    Args:
        monkeypatch: Pytest fixture for patching objects during a test.

    Returns:
        None.
    """

    pkg = importlib.import_module("ds_common_test_py_lib")

    def fake_version(_: str) -> str:
        raise importlib_metadata.PackageNotFoundError("ds-common-test-py-lib")

    monkeypatch.setattr(importlib_metadata, "version", fake_version)

    reloaded = importlib.reload(pkg)
    assert reloaded.__version__ == "0.0.0"
