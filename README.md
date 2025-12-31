# Calculator Package

A modular Python calculator engine providing basic and scientific calculation capabilities. This package is designed to
be used as a standalone CLI tool or as a library for external GUIs.

## 🚀 Features

* **Basic Operations:** Addition, Subtraction, Multiplication, Division.
* **Scientific Suite:** Square root, Trigonometry (Sine, Tangent), Factorials, and Logarithms.
* **Error Handling:** Robust handling for division by zero and invalid mathematical domains.

---

## 🛠️ Installation for Developers

If you want to clone this repository and install it locally to use in your own projects , follow these
steps:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/calculator.git
cd calculator

```

### 2. Install the Package Locally

You can install the package in **editable mode**. This means any changes you make to the code will immediately reflect
in your project without needing to reinstall.

```bash
pip install -e .
```

---

## 💻 Usage

### As a Command Line Tool

Once installed, you can run the calculator directly from your terminal:

```bash
calculator

```

### As a Module in your code

To use this engine in an external GUI project, simply import the modules:

```python
from src.calculator import basic, scientific

result = basic.addition(10, 5)
print(f"Result: {result}")

```

---

## 📦 Building the Wheel

To generate a `.whl` distribution file for production:

1. Install the build tool: `pip install build`
2. Run the build: `python -m build`
3. Find your file in the `dist/` folder.

---

## 🧪 Testing

To test the module logic without installing:

```bash
# Move to the root directory
cd ..
python -m calculator

```
