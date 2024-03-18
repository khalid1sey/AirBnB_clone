# 0x00. AirBnB clone - The console


## Table of Contents
- [AirBnB Clone Project Tasks](#airbnb-clone-project-tasks)
- [Introduction] (#Introduction)
- [Concepts] (#1 Concepts on this topic)
- [Steps] (#2.Steps)
- [Guidlines] (#3.Guidlines)


# Introduction
## First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

* put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine

## What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object



# 1 . Concepts on this topic

## 1. Creating a Python Package
To create a Python package, follow these steps:

1. Organize your code into a directory structure.
2. Create a `setup.py` file to provide package metadata and installation instructions.
3. Include an `__init__.py` file in each directory to mark it as a Python package.
4. Optionally, provide a `README.md` file to document your package.

## 2. Implementing a Command Interpreter using the `cmd` Module
The `cmd` module in Python provides a framework for creating command-line interpreters. To implement a command interpreter:

1. Import the `cmd` module.
2. Create a class that inherits from `cmd.Cmd`.
3. Define methods in the class to handle commands.
4. Use the `cmdloop()` method to start the command loop.

## 3. Unit Testing in Large Projects
Unit testing is the process of verifying that individual units of code work as expected. In large projects, it is essential to ensure the stability and correctness of the codebase. To implement unit testing:

1. Choose a testing framework such as `unittest` or `pytest`.
2. Write test cases for each unit of code.
3. Execute the tests using the testing framework.

## 4. Serialization and Deserialization of a Class
Serialization is the process of converting an object into a format suitable for storage or transmission. Deserialization is the reverse process of reconstructing an object from its serialized form. To serialize and deserialize a class, you can use the `pickle` module in Python.

## 5. Reading and Writing JSON Files
JSON (JavaScript Object Notation) is a widely used data interchange format. To read and write JSON files in Python:

1. Import the `json` module.
2. Use the `json.load()` function to read a JSON file.
3. Use the `json.dump()` function to write data to a JSON file.

## 6. Managing Datetime
Python's `datetime` module provides classes for working with dates and times. You can use it to perform various operations, such as creating, manipulating, and formatting dates and times.

## 7. Understanding UUIDs
UUID (Universally Unique Identifier) is a 128-bit identifier that is guaranteed to be unique across all devices and time. It is often used to identify resources in distributed systems. Python provides the `uuid` module to generate and manipulate UUIDs.

## 8. Working with `*args` in Python
In Python, `*args` is used to pass a variable number of positional arguments to a function. It allows you to pass any number of arguments to a function without explicitly specifying them.

To use `*args`:

1. Define a function with `*args` in its parameter list.
2. Access the arguments inside the function using the `args` variable, which is a tuple.

## 9. Utilizing `**kwargs` in Python
Similar to `*args`, `**kwargs` allows you to pass a variable number of keyword arguments to a function. It enables you to pass named arguments of any number without explicitly specifying them.

To use `**kwargs`:

1. Define a function with `**kwargs` in its parameter list.
2. Access the arguments inside the function using the `kwargs` variable, which is a dictionary.

## 10. Handling Named Arguments in a Function
Python allows you to define functions with named arguments, which provide more clarity and flexibility when calling functions. To handle named arguments in a function:

1. Define a function with named arguments.
2. Call the function and pass arguments using the `name=value` syntax.

---
# 2. Steps

Step 1: Create the BaseModel class
- Create a file named `base_model.py` in the `models` directory.
- Define a class called `BaseModel` that will serve as the parent class for all other classes in the project.
- Implement the initialization, serialization, and deserialization methods in the `BaseModel` class.
- Include a `to_dict()` method that converts an instance into a dictionary representation.
- Include a `save()` method that serializes the instance and saves it to a JSON file.

Step 2: Implement serialization and deserialization flow
- Create a `FileStorage` class in the `models/engine` directory.
- Implement methods in the `FileStorage` class to handle serialization and deserialization of instances.
- Use the `json` module to convert instances to JSON strings and vice versa.
- Implement methods to save instances to a JSON file and load instances from the file.

Step 3: Create classes for AirBnB entities
- Create individual files for each class (e.g., `user.py`, `state.py`, `city.py`, `place.py`) in the `models` directory.
- Define classes for `User`, `State`, `City`, `Place`, and any other entities required for the AirBnB clone.
- Inherit the `BaseModel` class in each of these classes.

Step 4: Implement the FileStorage engine
- Update the `__init__.py` file in the `models` directory to import the `FileStorage` class.
- Implement a global variable `storage` that is an instance of `FileStorage`, allowing access to the file storage engine throughout the project.

Step 5: Create unit tests
- Create a `tests` directory in the root of your project.
- Write unit tests for each class you've implemented, ensuring that they function as expected.
- Include tests for serialization, deserialization, saving, and loading of instances using the `FileStorage` engine.

By following these steps, you will build the foundation for your AirBnB clone project. Remember to regularly run your unit tests to ensure all classes and functionalities are working correctly.


# 3.Guidlines
# Python Unit Tests

This repository includes unit tests for Python scripts. Please ensure that you follow the guidelines mentioned below when creating and organizing your unit tests.

## Guidelines

- Editors: You can use any of the following editors: vi, vim, emacs.
- File Format: Ensure that all your files end with a new line.
- Test Folder: Place all your test files inside a folder named `tests`.
- Unittest Module: Use the `unittest` module for writing your unit tests.
- Test File Format: All your test files should have the `.py` extension.
- Test File and Folder Naming: All your test files and folders should start with `test_`.
- File Organization: Organize your test files in the `tests` folder in the same structure as your project files.
  - For example, if your project file is `models/base_model.py`, the corresponding unit test should be located at `tests/test_models/test_base_model.py`.
- Test Execution: Execute all your tests using the command `python3 -m unittest discover tests`.
- Individual Test Execution: You can also test individual files using the command `python3 -m unittest tests/test_models/test_base_model.py`.
- Documentation: All modules, classes, and functions should have appropriate documentation.

## Documentation Guidelines

- Modules: All your modules should have documentation. You can use the command `python3 -c 'print(__import__("my_module").__doc__)'` to verify the presence of documentation.
- Classes: All your classes should have documentation. You can use the command `python3 -c 'print(__import__("my_module").MyClass.__doc__)'` to verify the presence of documentation.
- Functions (Inside and Outside a Class): All your functions should have documentation. You can use the commands `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'` to verify the presence of documentation.

We strongly encourage collaboration on test cases to ensure comprehensive coverage, including edge cases. By following these guidelines, you can create effective unit tests for your Python scripts.

# Python Unit Tests

This repository includes unit tests for Python scripts. Please ensure that you follow the guidelines mentioned below when creating and organizing your unit tests.

## Guidelines

- Editors: You can use any of the following editors: vi, vim, emacs.
- File Format: Ensure that all your files end with a new line.
- Test Folder: Place all your test files inside a folder named `tests`.
- Unittest Module: Use the `unittest` module for writing your unit tests.
- Test File Format: All your test files should have the `.py` extension.
- Test File and Folder Naming: All your test files and folders should start with `test_`.
- File Organization: Organize your test files in the `tests` folder in the same structure as your project files.
  - For example, if your project file is `models/base_model.py`, the corresponding unit test should be located at `tests/test_models/test_base_model.py`.
- Test Execution: Execute all your tests using the command `python3 -m unittest discover tests`.
- Individual Test Execution: You can also test individual files using the command `python3 -m unittest tests/test_models/test_base_model.py`.
- Documentation: All modules, classes, and functions should have appropriate documentation.

## Documentation Guidelines

- Modules: All your modules should have documentation. You can use the command `python3 -c 'print(__import__("my_module").__doc__)'` to verify the presence of documentation.
- Classes: All your classes should have documentation. You can use the command `python3 -c 'print(__import__("my_module").MyClass.__doc__)'` to verify the presence of documentation.
- Functions (Inside and Outside a Class): All your functions should have documentation. You can use the commands `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'` to verify the presence of documentation.

We strongly encourage collaboration on test cases to ensure comprehensive coverage, including edge cases. By following these guidelines, you can create effective unit tests for your Python scripts.


# 2.Getting Started

To use the command interpreter, follow the instructions below.

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

   ```shell
   $ git clone https://github.com/your-username/airbnb-clone.git
   $ cd airbnb-clone
   ```

2. Create a virtual environment (optional but recommended):

   ```shell
   $ python3 -m venv venv
   $ source venv/bin/activate
   ```

3. Install the dependencies:

   ```shell
   $ pip install -r requirements.txt
   ```

### Usage

1. Run the command interpreter:

   ```shell
   $ python console.py
   ```

2. Enter commands at the prompt `(hbnb)`. Available commands:

   - **create**: Creates a new instance of BaseModel, saves it to the JSON file, and prints the ID. Usage: `create <class name>`.
   - **show**: Prints the string representation of an instance based on the class name and ID. Usage: `show <class name> <id>`.
   - **destroy**: Deletes an instance based on the class name and ID. Usage: `destroy <class name> <id>`.
   - **all**: Prints the string representation of all instances based on the class name. Usage: `all [class name]`.
   - **update**: Updates an instance based on the class name and ID by adding or updating an attribute. Usage: `update <class name> <id> <attribute name> "<attribute value>"`.
   - **quit**: Exits the command interpreter.

### Examples

- Create a new User:

  ```shell
  (hbnb) create User
  ```

- Show a User instance:

  ```shell
  (hbnb) show User <user_id>
  ```

- Delete a User instance:

  ```shell
  (hbnb) destroy User <user_id>
  ```

- Show all instances of a class:

  ```shell
  (hbnb) all User
  ```

- Update an attribute of a User instance:

  ```shell
  (hbnb) update User <user_id> email "example@example.com"
  ```
