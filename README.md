# PYTHON TKINTER CALCULATOR.
In this a simple GUI(graphical user interface) calculator built with Python and Tkinter. It is developed as a learning project 
to explore Object-Oriented Programming (OOP).It performs basic arithmetic operations such as addition, subtraction, 
multiplication, and division. The user can input expressions and see the results displayed on the screen.

## Objectives
Learn the basics of python programming
Build a simple working application
Use AI tools to guide through development
Document the learning process for beginners

## Features
GUI interface: Built using Tkinter library, a python built-in library
Basic operations: addition, subtraction, multiplication, division, percentage
OOP Architecture: Logic encapsulated within a `Calculator` class for better state management
Clear button: To reset display
Handles decimals and chained operations
Error handling for invalid expressions

## Technology summary
# What is python?
Python is a high-level, interpreted, general-purpose programming language known for its simple readable syntax that emphasizes code clarity. It supports object-oriented, structured, and functional programming, making it highly versatile
for web development, data science, AI, and automation.

# What is tkinter?
Tkinter is the standard Python library for creating graphical user interfaces. It provides an object-oriented interface
to the cross-platform Tk GUI toolkit, and is included with most standard Python installations, making it easily 
accessible for beginners without requiring additional setup. It lets you create windows, buttons, labels, input fields 
and layout containers to build desktop applications
Real-world-use: Simple data entry forms,

## System requirements
Os: Windows, macOS, Linux
Python: Python 3.7 or higher
tkinter: built-in python library
Editor: VS code

## Setup and Installation
1. Verify python is installed:
     - Open terminal and run: `python --version`
     - If not installed, download it from: `https://www.python.org/downloads/`
        * For windows:
          - Check the box that says Add python.exe to PATH. This allows you to run Python from any command prompt window.
          - Select Install Now, which includes essential features like pip (package manager) and IDLE (integrated
             development environment).
        * For macOS:
           - The installer places the Python executable and libraries in the /Library/Frameworks/Python.framework directory.
           - You can also use the Homebrew package manager for installation by running `brew install python in the terminal`.
        * For linux:
           - Python is usually pre-installed, but you may need to update to a newer version using your system's package                    manager(e.g., sudo apt install python3 on Ubuntu/Debian).

2. Verify tkinter is available:
     - Run: `python -m tkinter`
3. Download the project:
   * Option A - clone with git
         `git clone https://github.com/KiokoB/python-calculator-project/`
          `cd python-calculator-project`
   * Option B - download the zip file from github, extract it and open the folder
4. Run the program:
     `python calculator.py`
    - The calculator window will open immediately, no additional dependencies are required

## Python structure
python-calculator-project
|__calculator.py - main application file
|__README.md

## How it works
A user inputs numbers and an operator, the calculator performs the operation and displays the results

## Common issues and fixes
1. python: command not found
     - Means python is not installed. Download it from python.org
2. Display shows error
     - Majorly due to entry of invalid expressions. Use the "C" to clear and re-enter.


