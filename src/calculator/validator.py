from enum import Enum
from typing import Any


class AngleUnit(str, Enum):
    """
    Units for angular calculations.
    Using str inheritance allows for easy comparison and serialization.
    """

    DEG = "deg"
    RAD = "rad"


def ensure_float(value: Any) -> float:
    """
    Convert input to float

    Args:
        value: The value to convert.

    Returns:
        float: The converted numeric value.

    Raises:
        TypeError: If the value is a boolean or not convertible to float.
    """
    if isinstance(
        value, bool
    ):  # Explicitly block bools because float(True) returns 1.0 without error
        raise TypeError("Expected number, got bool")
    try:
        return float(value)
    except (TypeError, ValueError):
        # Catch the errors that float() throws for strings or objects
        raise TypeError(f"Expected number, got {type(value).__name__}")
