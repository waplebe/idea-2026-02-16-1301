import argparse

def main():
    parser = argparse.ArgumentParser(description="A simple command-line todo list.")
    parser.add_argument("task", nargs='*', help="The task to add.")
    parser.add_argument("--remove", nargs='?', help="The task to remove.")
    parser.add_argument("--clear", action="store_true", help="Clear all tasks.")

    args = parser.parse_args()

    if args.task:
        print("Tasks:")
        for task in args.task:
            print(f"- {task}")

        # Add persistence using a file
        try:
            with open("todo.txt", "a") as f:
                for task in args.task:
                    f.write(task + "\n")
        except Exception as e:
            print(f"Error writing to file: {e}")

    if args.remove:
        try:
            with open("todo.txt", "r") as f:
                tasks = [line.strip() for line in f.readlines()]

            if args.remove in tasks:
                tasks.remove(args.remove)
                with open("todo.txt", "w") as f:
                    for task in tasks:
                        f.write(task + "\n")
                print(f"Removed task: {args.remove}")
            else:
                print(f"Task not found: {args.remove}")
        except Exception as e:
            print(f"Error reading/writing to file: {e}")

    if args.clear:
        try:
            with open("todo.txt", "w") as f:
                f.write("")
            print("All tasks cleared.")
        except Exception as e:
            print(f"Error clearing file: {e}")


if __name__ == "__main__":
    main()