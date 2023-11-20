class ToDoListManager():
    def __init__(self):
        self.to_do_list = {}

    def add_new_task(self, task):
        self.to_do_list[task] = 'To Do'
    
    def set_task_in_progress(self, task):
        if task in self.to_do_list:
            self.to_do_list[task] = 'In Progress'

    def complete_task(self, task):
        if task in self.to_do_list:
            self.to_do_list[task] = 'Completed'

    def delete_task(self, task):
        del self.to_do_list[task]

    def list_incomplete_tasks(self):
        incomplete_tasks = []
        for task in self.to_do_list:
            if self.to_do_list[task] != 'Completed':
                incomplete_tasks.append(task)
        return incomplete_tasks
    
    def len_to_do_list(self):
        return len(self.to_do_list)
