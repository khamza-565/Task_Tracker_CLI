# Task Tracker CLI

A simple command-line application for tracking tasks using Python.

## Features

- Add new tasks
- Update task descriptions
- Delete tasks
- Mark tasks as in progress or done
- List all tasks
- Filter tasks by status
- List incomplete tasks
- Store tasks in a JSON file

## Requirements

- Python 3
- No external libraries required

## Usage

Run commands from the terminal in the project directory.

### Add a task

```bash
python task_cli.py add "Buy groceries"
```

### Update a task

```bash
python task_cli.py update 1 "Buy groceries and milk"
```

### Delete a task

```bash
python task_cli.py delete 1
```

### Change task status

```bash
python task_cli.py mark-in-progress 1
python task_cli.py mark-done 1
```

### List tasks

```bash
python task_cli.py list
python task_cli.py list to-do
python task_cli.py list in-progress
python task_cli.py list done
python task_cli.py list incomplete
```

## Data Storage

Tasks are stored in `tasks.json`, which is created automatically when needed.
