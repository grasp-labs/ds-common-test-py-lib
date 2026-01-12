"""
File: test_greet.py
Description: Unit tests for ds_common_test_py_lib.greet.
Region: packages/shared
"""

from __future__ import annotations

import pytest

from ds_common_test_py_lib.greet import greet


def test_greet_returns_expected_string() -> None:
    """
    Verify greet returns the expected greeting.

    Returns:
        None.
    """

    assert greet("John", "Doe") == "Hello, John Doe!"


def test_greet_strips_whitespace() -> None:
    """
    Verify greet trims whitespace around the name.

    Returns:
        None.
    """

    assert greet("  Alice  ", "  Doe  ") == "Hello, Alice Doe!"


def test_greet_raises_for_empty_name() -> None:
    """
    Verify greet raises ValueError for empty/whitespace-only names.

    Returns:
        None.
    """

    with pytest.raises(ValueError, match="first_name must be a non-empty string"):
        greet("", "Doe")

    with pytest.raises(ValueError, match="last_name must be a non-empty string"):
        greet("John", "   ")
