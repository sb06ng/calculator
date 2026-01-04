import ast
import operator

from .. import basic, scientific
from ..validator import AngleUnit

# Maps AST operator types to our refactored basic logic
operators = {
    ast.Add: basic.add,
    ast.Sub: basic.subtract,
    ast.Mult: basic.multiply,
    ast.Div: basic.divide,
    ast.USub: operator.neg,
}

# Maps string function names to our refactored scientific logic
# Note: Since sine/tangent now require an AngleUnit, we use a lambda or partial
functions = {
    'sin': lambda x: scientific.calculate_sine(x, unit=AngleUnit.DEG),
    'tan': lambda x: scientific.calculate_tangent(x, unit=AngleUnit.DEG),
    'sqrt': scientific.calculate_sqrt,
    'log': scientific.calculate_log,
    'fac': scientific.calculate_factorial,
    'pow': scientific.calculate_power
}


def evaluate_node(node):
    """
    Recursively evaluates an AST node using the package's validated logic.
    """
    if isinstance(node, ast.Constant):
        return node.value

    elif isinstance(node, ast.BinOp):
        left = evaluate_node(node.left)
        right = evaluate_node(node.right)
        # This will now trigger our 'Add failed: ...' error messages
        return operators[type(node.op)](left, right)

    elif isinstance(node, ast.UnaryOp):
        return operators[type(node.op)](evaluate_node(node.operand))

    elif isinstance(node, ast.Call):
        func_name = node.func.id
        if func_name not in functions:
            raise NameError(f"Function '{func_name}' is not supported.")

        args = [evaluate_node(arg) for arg in node.args]
        return functions[func_name](*args)

    else:
        raise TypeError(f"Unsupported expression node: {type(node).__name__}")


def calculate(equation: str):
    """
    Parses a string equation and returns the calculated result.

    Example: "sqrt(25) + 5" -> 10.0
    """
    try:
        tree = ast.parse(equation, mode="eval")
        return evaluate_node(tree.body)
    except Exception as e:
        raise ValueError(f"Invalid Expression: {e}")
