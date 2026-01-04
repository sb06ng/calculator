import math


def sqrt(a):
    """
    Calculates the square root of a number.

    Args:
        a (int, float): The number to process.

    Returns:
        float: The square root of the number.

    Raises:
        ValueError: If 'a' is a negative number.
        TypeError: If 'a' is not a numeric type.
    """
    if not isinstance(a, (int, float)):
        raise TypeError(f"Expected number, got {type(a).__name__}")
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(a)


def power(base, exponent):
    """
    Raises a base to a specific power.

    Args:
        base (int, float): The number to be multiplied.
        exponent (int, float): The power to raise the base to.

    Returns:
        float: The result of base**exponent.
    Raises:
        TypeError: If 'base' or 'exponent' is not a numeric type.
    """
    if not isinstance(base, (int, float)):
        raise TypeError(f"Expected number for base, got {type(base).__name__}")
    if not isinstance(exponent, (int, float)):
        raise TypeError(f"Expected number for exponent, got {type(exponent).__name__}")
    return math.pow(base, exponent)


def sine(angle, in_degrees=True):
    """
    Calculates the sine of an angle.

    Args:
        angle (int, float): The angle to calculate.
        in_degrees (bool): If True, treats angle as degrees. If False, as radians.
            Defaults to True.

    Returns:
        float: The sine of the angle.

    Raises:
        TypeError: If 'angle' is not a numeric type.
    """
    if not isinstance(angle, (int, float)):
        raise TypeError(f"Expected number, got {type(angle).__name__}")
    if in_degrees:
        angle = math.radians(angle)
    return math.sin(angle)


def log(x, base=math.e):
    """
    Calculates the logarithm of x to the given base.

    Args:
        x (int, float): The number to find the logarithm of.
        base (int, float, optional): The logarithmic base. Defaults to e (natural log).

    Returns:
        float: The logarithm of x.

    Raises:
        ValueError: If x is less than or equal to 0.
        TypeError: If x or base is not a numeric type.
    """
    if not isinstance(x, (int, float)):
        raise TypeError(f"Expected number, got {type(x).__name__}")
    if not isinstance(base, (int, float)):
        raise TypeError(f"Expected number, got {type(base).__name__}")
    if x <= 0:
        raise ValueError("Logarithm undefined for values <= 0.")
    return math.log(x, base)


def factorial(n):
    """
    Calculates the factorial of a non-negative integer.

    Args:
        n (int): The number to calculate.

    Returns:
        int: The factorial of n.

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("Factorial requires an integer.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(n)


def tangent(angle, in_degrees=True):
    """
    Calculates the tangent of an angle.

    Args:
        angle (int, float): The angle to calculate.
        in_degrees (bool): If True, treats angle as degrees. Defaults to True.

    Returns:
        float: The tangent of the angle.

    Raises:
        ValueError: If the angle is at a point where tangent is undefined (e.g., 90°).
        TypeError: If angle is not a numeric type.
    """
    if not isinstance(angle, (int, float)):
        raise TypeError(f"Expected number, got {type(angle).__name__}")
    if in_degrees:
        # Check for undefined points in degrees (90, 270, etc.)
        if (angle - 90) % 180 == 0:
            raise ValueError(f"Tangent is undefined for {angle} degrees.")
        angle = math.radians(angle)

    return math.tan(angle)


__all__ = [
    sqrt.__name__,
    power.__name__,
    sine.__name__,
    log.__name__,
    factorial.__name__,
    tangent.__name__,
]
