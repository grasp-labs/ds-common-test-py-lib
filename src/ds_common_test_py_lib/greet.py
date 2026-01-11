"""
File: greet.py
Description: Minimal entrypoint and helpers used for repository smoke tests.
Region: packages/shared
"""

from __future__ import annotations


def greet(name: str) -> str:
    """
    Build a friendly greeting.

    Args:
        name: Name to greet. Must be a non-empty string after stripping.

    Returns:
        A greeting string.

    Raises:
        ValueError: If name is empty or only whitespace.

    Example:
        >>> greet("World")
        'Hello, World!'
    """

    cleaned_name = name.strip()
    if cleaned_name == "":
        raise ValueError("name must be a non-empty string")

    return f"Hello, {cleaned_name}!"
