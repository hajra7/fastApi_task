# app.py

from fastapi import FastAPI, Form, Request, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from models import Task, tasks, task_id_counter

app = FastAPI()
templates = Jinja2Templates(directory="templates")


# Route to display all tasks
@app.get("/")
async def task_list(request: Request):
    return templates.TemplateResponse("task_list.html", {"request": request, "tasks": tasks})

# Route to add a new task
@app.get("/add")
async def add_task_form(request: Request):
    return templates.TemplateResponse("add_task.html", {"request": request})

@app.post("/add")
async def add_task(title: str = Form(...)):
    global task_id_counter
    new_task = Task(id=task_id_counter, title=title)
    tasks.append(new_task)
    task_id_counter += 1
    return RedirectResponse("/", status_code=303)

# Route to edit a task
@app.get("/edit/{id}")
async def edit_task_form(request: Request, id: int):
    task = next((t for t in tasks if t.id == id), None)
    if not task:
        return RedirectResponse("/", status_code=303)
    return templates.TemplateResponse("edit_task.html", {"request": request, "task": task})

@app.post("/edit/{id}")
async def edit_task(id: int, title: str = Form(...), completed: bool = Form(False)):
    task = next((t for t in tasks if t.id == id), None)
    if task:
        task.title = title
        task.completed = completed
    return RedirectResponse("/", status_code=303)

# Route to delete a task
@app.post("/delete/{id}")
async def delete_task(id: int):
    global tasks
    tasks = [t for t in tasks if t.id != id]
    return RedirectResponse("/", status_code=303)
