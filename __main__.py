from . import basic


def main():
    x, y = 100, 10
    print(f"x = {x}, y = {y}")

    print(f"x + y = {basic.addition(x, y)}")

    print(f"x - y = {basic.subtraction(x, y)}")

    print(f"x * y = {basic.multiplication(x, y)}")

    print(f"x / y = {basic.division(x, y)}")


if __name__ == '__main__':
    main()
