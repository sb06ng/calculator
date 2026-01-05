import math

from .validator import ensure_float, AngleUnit

DEFAULT_LOG_BASE = 2


def calculate_sqrt(number: float) -> float:
    """
    Calculate the square root of a number.

    Args:
        number: The number to process.

    Returns:
        float: The square root of the number.

    Raises:
        ValueError: If the number is negative.
        TypeError: If the input is not a number or is a boolean.
    """
    try:
        val = ensure_float(number)
        if val < 0:
            raise ValueError("Cannot calculate square root of a negative number.")
        return math.sqrt(val)
    except (TypeError, ValueError) as error:
        raise type(error)(f"Sqrt failed: {error}") from error


def calculate_power(base: float, exponent: float) -> float:
    """
    Raise a base to a specific power.

    Args:
        base: The base number.
        exponent: The power to raise the base to.

    Returns:
        float: The result of base raised to the exponent.

    Raises:
        TypeError: If base or exponent are not numbers.
    """
    try:
        return math.pow(ensure_float(base), ensure_float(exponent))
    except TypeError as error:
        raise TypeError(f"Power failed: {error}") from error


def calculate_sine(angle: float, unit: AngleUnit = AngleUnit.DEG) -> float:
    """
    Calculate the sine of an angle.

    Args:
        angle: The numeric value of the angle.
        unit: The unit of the angle (AngleUnit.DEG or AngleUnit.RAD).

    Returns:
        float: The sine of the angle.

    Raises:
        TypeError: If angle is not a number.
        ValueError: If unit is not valid.
    """
    try:
        angle_val = ensure_float(angle)

        if unit == AngleUnit.DEG:
            angle_val = math.radians(angle_val)
        elif unit == AngleUnit.RAD:
            pass
        else:
            raise ValueError(f"Invalid unit. Use {AngleUnit.DEG} or {AngleUnit.RAD}")

        return math.sin(angle_val)
    except (TypeError, ValueError) as error:
        raise type(error)(f"Sine failed: {error}") from error


def calculate_log(number: float, base: float = DEFAULT_LOG_BASE) -> float:
    """
    Calculate the logarithm of a number to a given base.

    Args:
        number: The value to find the logarithm of.
        base: The logarithmic base.

    Returns:
        float: The logarithm of the number.

    Raises:
        ValueError: If number <= 0 or base <= 0 or base == 1.
        TypeError: If number or base are not numbers.
    """
    try:
        val = ensure_float(number)
        base_val = ensure_float(base)

        if val <= 0:
            raise ValueError("Logarithm number must be > 0.")
        if base_val <= 0 or base_val == 1:
            raise ValueError("Logarithm base must be > 0 and not equal to 1.")

        return math.log(val, base_val)
    except (TypeError, ValueError) as error:
        raise type(error)(f"Log failed: {error}") from error


def calculate_factorial(number: int) -> int:
    """
    Calculate the factorial of a non-negative integer.

    Args:
        number: The whole integer to calculate.

    Returns:
        int: The factorial result.

    Raises:
        TypeError: If input is not a whole integer or is a boolean.
        ValueError: If number is negative.
    """
    try:
        if isinstance(number, bool) or not isinstance(number, int):
            raise TypeError("Factorial requires a whole integer.")

        if number < 0:
            raise ValueError("Factorial is not defined for negative numbers.")

        return math.factorial(number)
    except (TypeError, ValueError) as error:
        raise type(error)(f"Factorial failed: {error}") from error


def calculate_tangent(angle: float, unit: AngleUnit = AngleUnit.DEG) -> float:
    """
    Calculate the tangent of an angle.

    Args:
        angle: The numeric value of the angle.
        unit: The unit of the angle (AngleUnit.DEG or AngleUnit.RAD).

    Returns:
        float: The tangent of the angle.

    Raises:
        ValueError: If the tangent is undefined at the given angle.
        TypeError: If angle is not a number.
    """
    try:
        angle_val = ensure_float(angle)

        if unit == AngleUnit.DEG:
            if (angle_val - 90) % 180 == 0:
                raise ValueError(f"Tangent is undefined for {angle_val} degrees.")
            angle_val = math.radians(angle_val)
        elif unit == AngleUnit.RAD:
            # Undefined check for radians: tan(x) is undefined at (pi/2) + k*pi
            # Check if the value is very close to (pi/2) to catch math errors
            if (angle_val - (math.pi / 2)) % math.pi == 0:
                raise ValueError(f"Tangent is undefined for {angle_val} radians.")
        else:
            raise ValueError(f"Invalid unit. Use {AngleUnit.DEG} or {AngleUnit.RAD}")

        return math.tan(angle_val)
    except (TypeError, ValueError) as error:
        raise type(error)(f"Tangent failed: {error}") from error


__all__ = [
    calculate_sqrt.__name__,
    calculate_power.__name__,
    calculate_sine.__name__,
    calculate_log.__name__,
    calculate_factorial.__name__,
    calculate_tangent.__name__,
]
