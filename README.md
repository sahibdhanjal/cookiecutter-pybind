# CookieCutter-PyBind
This project provides a template to quickly bootstrap Python/C++ projects that utilize PyBind11 for interoperability.

## Getting Started
To set up your own PyBind project using this template:

1. **Fork the Repository**: Fork this repository on your preferred Git hosting platform.

2. **Clone with Submodules**: When cloning the repository, use the `--recursive` flag to ensure the pybind submodule is also downloaded:
    ``` bash
    git clone --recursive https://<your-fork-url>
    ```
3. **Build and Install**:
While developing locally, you can install the project for testing purposes using these two options:
- Use `pip`:
    ``` Bash
    pip install -e .
    ```
- Use `setuptools`:
    ```Bash
    python setup.py install
    ```
4. **Usage Example** : Refer to the test/test.py file for an example of how to use the generated project structure. You can also run the tests after installation:

    ```bash
    python test/test.py
    ```

## Submodules vs. Local Cloning
This template utilizes Git submodules to manage the pybind dependency. Submodules offer several advantages over manually cloning the dependency into your project:

- **Reduced Repository Size**: Submodules only store the reference to the dependency, not the actual code.
- **Centralized Updates**: Updates to the `pybind` submodule are managed independently, ensuring compatibility with your project.

## Learning More
For a deeper understanding of PyBind11 and calling C/C++ from Python, refer to this article:
- [Beyond Python's Limits: Calling the C++ Cavalry with PyBind11](https://medium.com/@sahibdhanjal/beyond-pythons-limits-calling-the-c-cavalry-with-pybind11-377b0b429a81)

The article clarifies the steps, explains benefits of submodules, and removes the unnecessary informality.
