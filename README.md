## 🚀 Installation

Clone the repo to your local environment

```bash
git clone https://github.com/sb06ng/calculator
```

Move to the root directory

```bash
cd calculator
```

From the root directory (where `pyproject.toml` is located):

```bash
pip install .
```

---

## 🛠 Usage

### Basic Arithmetic

The `basic` module provides standard operations. Note that all results are returned as `float`.

```python
from calculator.basic import add, divide

# Simple addition
print(add(10, 5))  # Output: 15.0

# Division with error handling
try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(e)  # Output: Divide failed: Division by zero is not allowed.
```

### Scientific Calculations

The `scientific` module handles advanced math. For trigonometric functions, use the `AngleUnit` Enum.

```python
from calculator.scientific import calculate_sine, calculate_log
from calculator.validator import AngleUnit

# Sine using Degrees (Default)
print(calculate_sine(90, unit=AngleUnit.DEG))  # Output: 1.0

# Natural Log (Default base is e)
print(calculate_log(10))

# Log with custom base
print(calculate_log(100, base=10))  # Output: 2.0
```

## 🧪 Development & Testing

To run the package in development mode:

1. Clone the repository.
2. Install in editable mode: `pip install -e .`
3. Run your scripts using absolute imports: `python -m calculator`
