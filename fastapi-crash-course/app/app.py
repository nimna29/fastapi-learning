from fastapi import FastAPI

app = FastAPI(
    title="FastAPI CRUD - To-Do App",
    description="FastAPI Crash Course",
    version="0.0.0"
)

# Minimal app - get request
@app.get("/", tags=['ROOT'])
async def root() -> dict:
    return {"message": "Hello World"}

# Get --> Read List of Todos
@app.get('/todo', tags=['todos'])
async def get_todos() -> dict:
    return {"data": todos}

# Post --> Create Todo
@app.post('/todo', tags=['todos'])
async def create_todos(todo: dict) -> dict:
    todos.append(todo)
    return {
        "data": "Todo added!!"
    }

# Put --> Update Todo
@app.put('/todo/{id}', tags=['todos'])
async def update_todos(id: int, body: dict) -> dict:
    for todo in todos:
        if int(todo['id']) == id:
            todo['activity'] = body['activity']
            return {
                "data": f"Todo with id {id} has been updated!!"
            }
    return {
        "data": f"Todo with id {id} not found!!"
    }

# Delete --> Delete Todo
@app.delete('/todo/{id}', tags=['todos'])
async def delete_todos(id: int) -> dict:
    for todo in todos:
        if int(todo['id']) == id:
            todos.remove(todo)
            return {
                "data": f"Todo with id {id} has been deleted!!"
            }
    return {
        "data": f"Todo with id {id} not found!!"
    }

# Example todos dict with id and activity
todos = [
    {
        "id": 1,
        "activity": "Learn Python"
    },
    {
        "id": 2,
        "activity": "Learn FastAPI"
    },
    {
        "id": 3,
        "activity": "Learn Docker"
    },
    {
        "id": 4,
        "activity": "Learn Kubernetes"
    },
    {
        "id": 5,
        "activity": "Learn AWS"
    }
]