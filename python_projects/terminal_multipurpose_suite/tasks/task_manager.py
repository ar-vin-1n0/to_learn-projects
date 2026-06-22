from task import Task

class TaskManager:
     def __init__(self):
         self.tasks = []
         self.next_id = 1

     def add_task(self,title):
         task = Task(self.next_id,
                     title)
         self.tasks.append(task)

         self.next_id += 1

     def list_tasks(self):
         if not self.tasks :
             return "No tasks available"
         else:
             result = []
             for task in self.tasks:
                 result.append(str(task))
             return result

     def find_task_by_id(self,show_task_by_id):
         for task in self.tasks:
             if task.task_id == show_task_by_id:
                 return task
         else:
            return "No task with that id found"

     def complete_task(self,show_task_by_id):
         task = self.find_task_by_id(show_task_by_id)
         task.mark_complete()

     def delete_task_by_id(self,show_task_by_id):
         for task in self.tasks:
             if task.task_id == show_task_by_id:
                 self.tasks.remove(task)
                 return f"removed task with id : {show_task_by_id}"
         else:
              return "No task with that id found"