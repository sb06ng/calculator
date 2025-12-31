def addition(a, b):
    """
    Add two numbers
    Args:
        a (int, float): First number
        b (int, float) : Second number

    Returns:
        number: Sum of two numbers

    Raises:
        TypeError: If 'a' or 'b' is not a number
    """
    if not isinstance(a, (int, float)):
        raise TypeError(f"Expected number for a, got {type(a).__name__}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"Expected number for b, got {type(b).__name__}")
    return a + b


def subtraction(a, b):
    """
    Subtract two numbers
    Args:
        a (int, float): First number
        b (int, float) : Second number

    Returns:
        number: Subtract two numbers

    Raises:
        TypeError: If 'a' or 'b' is not a number
    """
    if not isinstance(a, (int, float)):
        raise TypeError(f"Expected number for a, got {type(a).__name__}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"Expected number for b, got {type(b).__name__}")
    return a - b


def multiplication(a, b):
    """
    Multiply two numbers
    Args:
        a (int, float): First number
        b (int, float) : Second number

    Returns:
        number: Multiply two numbers

    Raises:
        TypeError: If 'a' or 'b' is not a number
    """
    if not isinstance(a, (int, float)):
        raise TypeError(f"Expected number for a, got {type(a).__name__}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"Expected number for b, got {type(b).__name__}")
    return a * b


def division(a, b):
    """
    Divide two numbers
    Args:
        a (int, float): First number
        b (int, float) : Second number

    Returns:
        number: Divide two numbers

    Raises:
        TypeError: If 'a' or 'b' is not a number
        ZeroDivisionError: If 'b' is zero
    """
    if not isinstance(a, (int, float)):
        raise TypeError(f"Expected number for a, got {type(a).__name__}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"Expected number for b, got {type(b).__name__}")

    if b == 0: raise ZeroDivisionError("division by zero")
    return a / b
