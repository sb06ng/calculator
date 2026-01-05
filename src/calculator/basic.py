from .validator import ensure_float


def add(first_number: float, second_number: float) -> float:
    """
    Add two numbers and return a float result.

    Args:
        first_number: The first number to add.
        second_number: The second number to add.

    Returns:
        float: The sum of the two numbers.

    Raises:
        TypeError: If inputs are booleans or not numbers.
    """
    try:
        return ensure_float(first_number) + ensure_float(second_number)
    except TypeError as error:
        raise TypeError(f"Add failed: {error}")


def subtract(first_number: float, second_number: float) -> float:
    """
    Subtract the second number from the first and return a float result.

    Args:
        first_number: The number to be subtracted from.
        second_number: The number to subtract.

    Returns:
        float: The difference as a float.

    Raises:
        TypeError: If inputs are booleans or not numbers.
    """
    try:
        return ensure_float(first_number) - ensure_float(second_number)
    except TypeError as error:
        raise TypeError(f"Subtract failed: {error}")


def multiply(first_number: float, second_number: float) -> float:
    """
    Multiply two numbers and return a float result.

    Args:
        first_number: The first factor.
        second_number: The second factor.

    Returns:
        float: The product as a float.

    Raises:
        TypeError: If inputs are booleans or not numbers.
    """
    try:
        return ensure_float(first_number) * ensure_float(second_number)
    except TypeError as error:
        raise TypeError(f"Multiply failed: {error}")


def divide(first_number: float, second_number: float) -> float:
    """
    Divide the first number by the second and return a float result.

    Args:
        first_number: The dividend.
        second_number: The divisor.

    Returns:
        float: The quotient as a float.

    Raises:
        TypeError: If inputs are booleans or not numbers.
        ZeroDivisionError: If the second_number is zero.
    """
    try:
        num1 = ensure_float(first_number)
        num2 = ensure_float(second_number)
        return num1 / num2
    except TypeError as error:
        raise TypeError(f"Divide failed: {error}")
    except ZeroDivisionError:
        raise ZeroDivisionError("Divide failed: Division by zero is not allowed.")


__all__ = [
    add.__name__,
    subtract.__name__,
    multiply.__name__,
    divide.__name__
]
