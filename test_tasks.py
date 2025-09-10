
import unittest
from tasks import TaskManager

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Test task")
        self.assertEqual(task.description, "Test task")
        self.assertEqual(task.status, "todo")
        self.assertEqual(len(self.manager.tasks), 1)

    def test_update_task(self):
        task = self.manager.add_task("Old description")
        updated = self.manager.update_task(task.id, "New description")
        self.assertTrue(updated)
        self.assertEqual(self.manager.tasks[task.id].description, "New description")

    def test_delete_task(self):
        task = self.manager.add_task("Task to delete")
        deleted = self.manager.delete_task(task.id)
        self.assertTrue(deleted)
        self.assertEqual(len(self.manager.tasks), 0)

    def test_mark_done(self):
        task = self.manager.add_task("Complete me")
        self.manager.mark_done(task.id)
        self.assertEqual(self.manager.tasks[task.id].status, "done")

    def test_mark_in_progress(self):
        task = self.manager.add_task("Work in progress")
        self.manager.mark_in_progress(task.id)
        self.assertEqual(self.manager.tasks[task.id].status, "in-progress")

    def test_list_tasks(self):
        t1 = self.manager.add_task("Task 1")
        t2 = self.manager.add_task("Task 2")
        self.manager.mark_done(t1.id)
        done_tasks = self.manager.list_tasks("done")
        todo_tasks = self.manager.list_tasks("todo")
        self.assertEqual(len(done_tasks), 1)
        self.assertEqual(len(todo_tasks), 1)

if __name__ == "__main__":
    unittest.main()
