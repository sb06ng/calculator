from . import basic
from . import scientific


def main():
    print("Testing basic calculations...")
    x, y = 100, 10
    print(f"x = {x}, y = {y}")

    print(f"x + y = {basic.add(x, y)}")

    print(f"x - y = {basic.subtract(x, y)}")

    print(f"x * y = {basic.multiply(x, y)}")

    print(f"x / y = {basic.divide(x, y)}")

    val = 25
    print(f"The square root of {val} is: {scientific.calculate_sqrt(val)}")

    deg = 90
    print(f"The sine of {deg} degrees is: {scientific.calculate_sine(deg)}")

    try:
        print("Testing error handling...")
        scientific.calculate_log(-1)
    except (ValueError, TypeError) as e:
        print(f"Calculation Error: {e}")

    print(f"ln({y}): {scientific.calculate_log(y)}")

    print(f"log{y}({x}): {scientific.calculate_log(x, y)}")

    print(f"{y}! is: {scientific.calculate_factorial(y)}")

    try:
        print(f"Tan of 90: {scientific.calculate_tangent(90)}")
    except ValueError as e:
        print(f"Caught expected error: {e}")


if __name__ == '__main__':
    main()
