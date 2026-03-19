import unittest
from main import main
import os

class TestMain(unittest.TestCase):

    def setUp(self):
        # Create a temporary todo.txt file for testing
        if not os.path.exists("todo.txt"):
            with open("todo.txt", "w") as f:
                f.write("")

    def tearDown(self):
        # Remove the temporary todo.txt file after testing
        if os.path.exists("todo.txt"):
            os.remove("todo.txt")

    def test_add_tasks(self):
        main(["task1", "task2"])
        with open("todo.txt", "r") as f:
            tasks = [line.strip() for line in f.readlines()]
        self.assertEqual(tasks, ["task1", "task2"])

    def test_view_tasks(self):
        main()
        with open("todo.txt", "r") as f:
            tasks = [line.strip() for line in f.readlines()]
        self.assertGreaterEqual(len(tasks), 0)

    def test_remove_task(self):
        main(["task1", "task2"])
        with open("todo.txt", "r") as f:
            tasks = [line.strip() for line in f.readlines()]
        self.assertEqual(tasks, ["task1", "task2"])
        main(["task1", "--remove", "task1"])
        with open("todo.txt", "r") as f:
            tasks = [line.strip() for line in f.readlines()]
        self.assertEqual(tasks, ["task2"])

    def test_clear_tasks(self):
        main(["task1", "task2"])
        with open("todo.txt", "r") as f:
            tasks = [line.strip() for line in f.readlines()]
        self.assertEqual(tasks, ["task1", "task2"])
        main(["--clear"])
        with open("todo.txt", "r") as f:
            tasks = [line.strip() for line in f.readlines()]
        self.assertEqual(tasks, [])

    def test_remove_nonexistent_task(self):
        main(["task1", "--remove", "task2"])
        with open("todo.txt", "r") as f:
            tasks = [line.strip() for line in f.readlines()]
        self.assertEqual(tasks, ["task1"])

    def test_clear_empty_list(self):
        with open("todo.txt", "w") as f:
            f.write("")
        main(["--clear"])
        with open("todo.txt", "r") as f:
            tasks = [line.strip() for line in f.readlines()]
        self.assertEqual(tasks, [])

    def test_add_task_with_spaces(self):
        main("Task with spaces")
        with open("todo.txt", "r") as f:
            tasks = [line.strip() for line in f.readlines()]
        self.assertEqual(tasks, ["Task with spaces"])

if __name__ == '__main__':
    unittest.main()