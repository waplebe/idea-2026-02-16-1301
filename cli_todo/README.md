# Simple CLI Todo List

This is a command-line tool for managing a todo list. It now includes the ability to remove tasks and persists the list to a file.

## Usage

**Adding Tasks:**

To add tasks, run the script with the task(s) as arguments:

```bash
python main.py task1 task2 task3
```

This will print the list of tasks to the console and add them to `todo.txt`.

**Viewing Tasks:**

To view the list, simply run the script without any arguments:

```bash
python main.py
```

This will read the tasks from `todo.txt` and print them to the console.

**Removing Tasks:**

To remove a task, use the `--remove` flag followed by the task to remove:

```bash
python main.py --remove task1
```

This will remove `task1` from `todo.txt` and update the displayed list.

**Clearing All Tasks:**

To clear all tasks, use the `--clear` flag:

```bash
python main.py --clear
```

This will empty the `todo.txt` file and update the displayed list.

## Persistence

The todo list is saved to a file named `todo.txt` in the project directory.  Each task is added to this file when you run the script with tasks as arguments, or removed when using the `--remove` flag.  To view the list, simply run the script without any arguments.

## Testing

Unit tests are included to ensure the functionality of the script.  Run them using:

```bash
python -m unittest cli_todo/main.py
```

## Example

```bash
# Add tasks
python main.py "Buy groceries" "Walk the dog" "Finish report"

# View tasks
python main.py

# Remove a task
python main.py --remove "Walk the dog"

# Clear all tasks
python main.py --clear
```