# Flask Todo App

This is a simple todo application built using Flask.

## Python version : 3.11.1

## Setup

1. Clone the repository:
    ```
    $ git clone https://github.com/vaibhav2808/TODO-flask/
    ```
2. Navigate to the project directory:
    ```
    $ cd TODO-flask
    ```
3. Create a virtual environment:
    ```
    $ python3 -m venv env
    ```
4. Activate the virtual environment:
    ```
    $ source env/bin/activate
    ```
5. Install dependencies:
    ```
    $ pip install -r requirements.txt
    ```
6. Start the Flask server:
    ```
    $ python app.py
    ```

## Endpoints

### POST /tasks

Creates a new task.

Parameters:

- `task` (required): the name of the task.

### DELETE /tasks/{id}

Deletes a task by ID.

### PUT /tasks/{id}

Updates a task by ID.

Parameters:

- `task` : the name of the task.


### PUT /tasks/{id}/complete

Marks a task as complete.

### PUT /tasks/{id}/incomplete

Marks a task as incomplete.

### PUT /tasks/{id}/toggle

Toggles the task. Marks task as completed if it was incomplete and vice versa

### GET /tasks

Returns a list of all tasks.

## Error handling

- 400 Bad Request
- 404 Not Found
- 500 Internal Server Error
