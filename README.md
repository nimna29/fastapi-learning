# FastAPI Learning Projects

Welcome to the FastAPI Learning repository! This collection of projects is designed to help you learn and explore FastAPI, a modern web framework for building APIs with Python.

## Overview of the Repository

This repository features four practical FastAPI projects, each with its own unique focus and learning opportunities:

### [simple-example](https://github.com/nimna29/fastapi-learning/tree/main/simple-example)
This project provides a straightforward example of FastAPI in action. It serves as a great starting point for understanding the basics of FastAPI development.

### [item-api](https://github.com/nimna29/fastapi-learning/tree/main/item-api)
In this project, you'll find a simple item management API with fundamental API endpoints. It's an excellent resource for getting hands-on experience with FastAPI for building RESTful services.

### [fastapi-crash-course](https://github.com/nimna29/fastapi-learning/tree/main/fastapi-crash-course)
This project introduces you to a To-do app built using FastAPI. You'll learn how to perform CRUD (Create, Read, Update, Delete) operations, a key skill for building robust APIs.

### [ml-with-fastapi](https://github.com/nimna29/fastapi-learning/tree/main/ml-with-fastapi)
In this project, you'll delve into the integration of FastAPI with a machine-learning model. It offers a practical example of how FastAPI can be used in real-world applications, particularly in ML-based projects.

🔥 Feel free to explore each project, experiment with the code, and expand your FastAPI knowledge.</br>Happy learning! 😎

---------------------------------------

## Setting Up the Development Environment

Follow these steps to set up your development environment for this project:

### Create a New `venv`

1. Navigate to your project directory:

   ```bash
   cd /path/to/your/project
   ```

2. Create a virtual environment:

   ```bash
   python -m venv <venv_name>
   ```

### Activate and Deactivate `venv`

- In `cmd`:

   ```bash
   <venv_name>\Scripts\activate
   ```

- In bash:

   ```bash
   source <venv_name>/Scripts/activate

   # To deactivate the virtual environment:
   deactivate
   ```

### Create, Activate & Deactivate `venv` using conda

- Use Anaconda Navigator to create a venv:

   ```
   # Activate the conda environment
   conda activate <venv_name>

   # To deactivate the conda environment
   conda deactivate
   ```

### Install the Dependencies

- You can also use a `requirements.txt` file to manage your project's dependencies. This file lists all the required packages and their versions.
1. Install packages from `requirements.txt`:

   ```
   pip install -r requirements.txt
   ```
    This ensures that your development environment matches the exact package versions specified in `requirements.txt`.

2. Verify installed packages:

   ```bash
   pip list
   ```
    This will display a list of packages currently installed in your virtual environment, including the ones from `requirements.txt`.

## Additional Requirements

For a smoother development experience, consider installing the following additional requirements:</br>
📝Note: FastAPI, Uvicorn, and Pydantic are listed inside the `requirements.txt`.

- [FastAPI](https://fastapi.tiangolo.com/): A modern web framework for building APIs with Python.

- [Uvicorn](https://www.uvicorn.org/): A lightning-fast ASGI server for running FastAPI applications.

- [Pydantic](https://docs.pydantic.dev/latest/): A data validation and parsing library.

- [Jupyter Notebook](https://jupyter.org/): An interactive computing environment for creating and sharing documents containing live code, equations, visualizations, and narrative text.

Feel free to install these requirements using `pip` or include them in your `requirements.txt` file if they are not already present.
You can include any additional requirements or tools that you find useful for your project development in the "Additional Requirements" section.

---------------------------------------------

## Running the Projects

Follow these steps to run the projects in your FastAPI Learning repository. Open your Bash terminal and navigate to the project directory:

```bash
cd <project_directory>
```

### For `simple-example` and `item-api` Projects:

1. To run the `simple-example` and `item-api` projects, use the following command:

   ```bash
   uvicorn main:app --reload
   ```

2. You can access the project output in your browser using the following URL:

   ```bash
   http://127.0.0.1:8000
   ```
3. To explore the API documentation, visit:

   ```bash
   http://127.0.0.1:8000/docs
   ```

### For `fastapi-crash-course` and `ml-with-fastapi` Projects:

1. To run the other two projects, use the following command:

   ```bash
   python main.py
   ```

2. You can access the project output in your browser using the following URL:

   ```bash
   http://127.0.0.1:8000
   ```
3. To explore the API documentation, visit:

   ```bash
   http://127.0.0.1:8000/docs
   ```

Enjoy exploring and running the FastAPI projects!

### `License`
This project is licensed under the MIT License. See [LICENSE](https://github.com/nimna29/fastapi-learning/blob/main/LICENSE) for more details.

-------------------------------

### `Credits`

I would like to extend my gratitude to the following sources for their valuable tutorials and resources that helped me learn and build the projects in this repository:

- **simple-example**
  - [YouTube Tutorial](https://www.youtube.com/watch?v=0RS9W8MtZe4)

- **item-api**
  - [YouTube Tutorial](https://www.youtube.com/watch?v=SORiTsvnU28)

- **fastapi-crash-course**
  - [YouTube Tutorial](https://www.youtube.com/watch?v=62pP9pfzNRs)

- **ml-with-fastapi**
  - [YouTube Tutorial](https://www.youtube.com/watch?v=b5F667g1yCk)

💡A big thank you to these creators for sharing their knowledge and helping the FastAPI community grow!

---------------------------------
