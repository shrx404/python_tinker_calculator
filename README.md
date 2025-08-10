# Python Tinker Calculator

A desktop calculator application built with Python and Tkinter, featuring multiple calculator interfaces with different designs and functionalities.

## 📋 Table of Contents

- [Features](#features)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technical Details](#technical-details)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### Calculator Interface 1 (`calculator.py`)
- **Basic Arithmetic Operations**: Addition, subtraction, multiplication, division
- **Clean Grid Layout**: Organized button arrangement using Tkinter's grid system
- **Black & White Theme**: Professional dark theme with white text
- **Clear Function**: Reset calculator display
- **Number Input**: Full numeric keypad (0-9)

### Calculator Interface 2 (`calculator_two.py`)
- **Advanced Operations**: Full mathematical expression evaluation using `eval()`
- **Modern UI Design**: Light gray background with white buttons
- **Decimal Support**: Includes decimal point functionality
- **Expression Builder**: Build complex mathematical expressions
- **Real-time Display**: Shows current expression as you type
- **Compact Layout**: Uses absolute positioning for precise button placement

### Application Launcher (`file_runner.py`)
- **Unified Interface**: Choose between different calculator versions
- **Easy Navigation**: Simple button-based selection
- **Modular Design**: Separate launcher for different calculator implementations

## 🖼️ Screenshots

### Calculator Interface 1
- Grid-based layout with black buttons
- Basic arithmetic operations
- Clean, professional appearance

### Calculator Interface 2
- Modern light gray interface
- Advanced expression evaluation
- Decimal point support
- More compact design

### Application Launcher
- Simple selection interface
- Two calculator options
- Easy switching between versions

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- Tkinter (usually comes pre-installed with Python)

### Step-by-Step Installation

1. **Clone or Download the Repository**
   ```bash
   git clone <repository-url>
   cd python_tinker_calculator
   ```

2. **Verify Python Installation**
   ```bash
   python --version
   # or
   python3 --version
   ```

3. **Check Tkinter Availability**
   ```bash
   python -c "import tkinter; print('Tkinter is available')"
   ```

4. **Install Dependencies** (if needed)
   ```bash
   pip install tkinter
   # Note: Tkinter is usually included with Python installation
   ```

## 💻 Usage

### Quick Start
1. **Run the Application Launcher**
   ```bash
   python file_runner.py
   ```

2. **Choose Your Calculator**
   - Click "calculator" for the basic grid-based interface
   - Click "calculator 2" for the advanced expression evaluator

### Direct Execution
You can also run individual calculator files directly:

```bash
# Run basic calculator
python calculator.py

# Run advanced calculator
python calculator_two.py
```

### Using the Calculators

#### Basic Calculator (Interface 1)
- Click number buttons to input values
- Use operation buttons (+, -, ×, ÷) for calculations
- Press "=" to see the result
- Use "clear" to reset the calculator

#### Advanced Calculator (Interface 2)
- Build mathematical expressions naturally
- Supports decimal numbers
- Use operators: +, -, *, /
- Press "=" to evaluate the entire expression
- Use "CE" to clear the display

## 📁 Project Structure

```
python_tinker_calculator/
├── README.md              # This documentation file
├── file_runner.py         # Application launcher and main entry point
├── calculator.py          # Basic calculator with grid layout
└── calculator_two.py      # Advanced calculator with expression evaluation
```

### File Descriptions

- **`file_runner.py`**: Main application launcher that provides a selection interface
- **`calculator.py`**: Basic calculator implementation using Tkinter grid layout
- **`calculator_two.py`**: Advanced calculator with expression evaluation capabilities
- **`README.md`**: Comprehensive project documentation

## 🔧 Technical Details

### Architecture
- **GUI Framework**: Tkinter (Python's standard GUI library)
- **Layout Systems**: Grid layout (calculator.py) and Absolute positioning (calculator_two.py)
- **Event Handling**: Button click events and lambda functions
- **Data Flow**: String-based input/output with mathematical evaluation

### Key Components

#### Calculator.py
- Uses `grid()` geometry manager for button arrangement
- Individual functions for each button click
- Global variable for storing first number in operations
- Basic arithmetic operations implementation

#### Calculator_two.py
- Uses `eval()` function for mathematical expression evaluation
- `StringVar()` for dynamic display updates
- Absolute positioning with `place()` geometry manager
- More sophisticated UI with better styling

#### File_runner.py
- Modular design with separate functions for each calculator
- Uses `os.system()` to launch calculator applications
- Simple selection interface

## 📋 Requirements

### System Requirements
- **Operating System**: Windows, macOS, or Linux
- **Python Version**: 3.6 or higher
- **Memory**: Minimal (less than 50MB RAM)
- **Storage**: Less than 1MB disk space

### Python Dependencies
```
tkinter (built-in with Python)
```

### Optional Dependencies
- **PyCharm IDE**: Recommended for development (as mentioned in original README)
- **Git**: For version control

## 🛠️ Development

### Setting Up Development Environment
1. **Install PyCharm** (recommended IDE)
2. **Open the project** in PyCharm
3. **Configure Python interpreter** if needed
4. **Run the application** using `file_runner.py`

### Code Style
- Follow PEP 8 Python style guidelines
- Use meaningful variable names
- Add comments for complex logic
- Maintain consistent indentation

### Testing
- Test both calculator interfaces
- Verify all arithmetic operations
- Check error handling for invalid inputs
- Test UI responsiveness

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Suggested Improvements
- Add more mathematical functions (square root, power, etc.)
- Implement keyboard support
- Add history functionality
- Improve error handling
- Add unit tests
- Create a more modern UI design

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built with Python and Tkinter
- Inspired by traditional desktop calculators
- Designed for educational and practical use

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](../../issues) page for existing problems
2. Create a new issue with detailed description
3. Include your operating system and Python version

---

**Note**: This calculator application is designed for educational purposes and basic calculations. For complex mathematical operations, consider using specialized mathematical software.
