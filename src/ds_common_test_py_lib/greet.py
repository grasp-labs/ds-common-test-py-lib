"""
File: greet.py
Description: Minimal entrypoint and helpers used for repository smoke tests.
Region: packages/shared
"""

from __future__ import annotations


def greet(first_name: str, last_name: str) -> str:
    """
    Build a friendly greeting.

    Args:
        first_name: First name to greet. Must be a non-empty string after stripping.
        last_name: Last name to greet. Must be a non-empty string after stripping.

    Returns:
        A greeting string.

    Raises:
        ValueError: If name is empty or only whitespace.

    Example:
        >>> greet("World")
        'Hello, World!'
    """

    cleaned_first_name = first_name.strip()
    cleaned_last_name = last_name.strip()
    if cleaned_first_name == "":
        raise ValueError("first_name must be a non-empty string")
    if cleaned_last_name == "":
        raise ValueError("last_name must be a non-empty string")

    return f"Hello, {cleaned_first_name} {cleaned_last_name}!"
