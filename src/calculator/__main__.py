from . import basic
from . import scientific


def main():
    x, y = 100, 10
    print(f"x = {x}, y = {y}")

    print(f"x + y = {basic.addition(x, y)}")

    print(f"x - y = {basic.subtraction(x, y)}")

    print(f"x * y = {basic.multiplication(x, y)}")

    print(f"x / y = {basic.division(x, y)}")

    val = 25
    print(f"The square root of {val} is: {scientific.sqrt(val)}")

    deg = 90
    print(f"The sine of {deg} degrees is: {scientific.sine(deg)}")

    try:
        print("Testing error handling...")
        scientific.sqrt(-1)
    except (ValueError, TypeError) as e:
        print(f"Calculation Error: {e}")

    print(f"ln({y}): {scientific.log(y)}")

    print(f"log{y}({x}): {scientific.log(x, y)}")

    print(f"{y}! is: {scientific.factorial(y)}")

    try:
        print(f"Tan of 90: {scientific.tangent(90)}")
    except ValueError as e:
        print(f"Caught expected error: {e}")


if __name__ == '__main__':
    main()
