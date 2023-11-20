import unittest
from to_do_list import ToDoListManager

class TestToDoListManager(unittest.TestCase):

    def test_add_task(self):
        to_do = ToDoListManager()
        to_do.add_new_task('Aula prática 5')
        expected = {'Aula prática 5': 'To Do'}
        self.assertEqual(to_do.to_do_list, expected)

    def test_set_task_in_progress_correct(self):
        to_do = ToDoListManager()
        to_do.add_new_task('Aula prática 5')
        to_do.set_task_in_progress('Aula prática 5')
        expected = {'Aula prática 5': 'In Progress'}
        self.assertEqual(to_do.to_do_list, expected)

    def test_set_task_in_progress_incorrect(self):
        to_do = ToDoListManager()
        to_do.set_task_in_progress('Aula prática 5')
        expected = {}
        self.assertEqual(to_do.to_do_list, expected)

    def test_complete_task_correct(self):
        to_do = ToDoListManager()
        to_do.add_new_task('Aula prática 5')
        to_do.complete_task('Aula prática 5')
        expected = {'Aula prática 5': 'Completed'}
        self.assertEqual(to_do.to_do_list, expected)

    def test_complete_task_incorrect(self):
        to_do = ToDoListManager()
        to_do.complete_task('Aula prática 5')
        expected = {}
        self.assertEqual(to_do.to_do_list, expected)

    def test_delete_task(self):
        to_do = ToDoListManager()
        to_do.add_new_task('Aula prática 5')
        to_do.add_new_task('Aula prática 4')
        to_do.complete_task('Aula prática 4')
        to_do.delete_task('Aula prática 4')
        expected = {'Aula prática 5': 'To Do'}
        self.assertEqual(to_do.to_do_list, expected)

    def test_list_incomplete_tasks(self):
        to_do = ToDoListManager()
        to_do.add_new_task('Aula prática 3')
        to_do.add_new_task('Aula prática 4')
        to_do.add_new_task('Aula prática 5')
        to_do.complete_task('Aula prática 3')
        to_do.set_task_in_progress('Aula prática 4')
        expected = ['Aula prática 4', 'Aula prática 5']
        self.assertEqual(to_do.list_incomplete_tasks(), expected)

    def test_len_to_do_list(self):
        to_do = ToDoListManager()
        to_do.add_new_task('Aula prática 3')
        to_do.add_new_task('Aula prática 4')
        to_do.add_new_task('Aula prática 5')
        self.assertEqual(to_do.len_to_do_list(), 3)


if __name__ == '__main__':
    unittest.main()