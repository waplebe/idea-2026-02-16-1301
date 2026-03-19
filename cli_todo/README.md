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

## Improvements

*   **Robust Error Handling:** Added comprehensive `try...except` blocks to handle potential file I/O errors gracefully.  This prevents the script from crashing if the `todo.txt` file is inaccessible or if there are permission issues.
*   **Non-Existent Task Removal:** Implemented a check to ensure that the task being removed actually exists in the `todo.txt` file. If the task is not found, a message is printed to the console, and the list remains unchanged.
*   **Empty List Clearing:** Added a test case and logic to handle the scenario where the `todo.txt` file is empty when the `--clear` flag is used.
*   **Tasks with Spaces:** Added a test case and logic to handle tasks containing spaces.
*   **Comprehensive Testing:** Added new test cases to cover edge cases such as removing a non-existent task and clearing an empty list.  This ensures that the script behaves correctly in various situations.
*   **Improved Documentation:** Updated the README file to reflect the new features and improvements.