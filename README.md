# 🚀 Installation

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

# 🛠 Usage

## 🖥️ Graphical User Interface (GUI)

The package includes a built-in GUI built with **Tkinter**. It allows for both simple button-based math and complex
expression parsing (e.g., typing `sqrt(25) + sin(90)` into a text field).

### Running the GUI

If you installed the package via `pip install .`, you can launch the interface directly from your terminal:

```bash
calculator
```

Alternatively, you can run it as a module:

```bash
python -m calculator
```

### Supported Expression Syntax

Because the GUI uses our `scientific` logic, you can type expressions using the following function aliases:

| Text Function | Package Function      | Default Unit |
|---------------|-----------------------|--------------|
| `sin(x)`      | `calculate_sine`      | Degrees      |
| `tan(x)`      | `calculate_tangent`   | Degrees      |
| `sqrt(x)`     | `calculate_sqrt`      | N/A          |
| `fac(x)`      | `calculate_factorial` | N/A          |
| `log(x, b)`   | `calculate_log`       | N/A          |

---

## 🔧 CLI vs GUI Mode

The package's entry point is configured to detect how you want to use the tool. By default, it launches the GUI, but it
can be used for automated testing via the command line.

* **Launch GUI:** `calculator`
* **Run CLI Tests:** `calculator --cli`

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

# 🧪 Development & Testing

To run the package in development mode:

1. Clone the repository.
2. Install in editable mode: `pip install -e .`
3. Run your scripts using absolute imports: `python -m calculator`

---
