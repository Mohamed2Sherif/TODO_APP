from .models import Task as Taskdb
from .dto import Task
from django.contrib.contenttypes.models import ContentType
def get_task_contenttype():
    contenttype = ContentType.objects.get_for_model(Task)
    return contenttype
def add_task_to_database(task:Task):
    taskdb = Taskdb.objects.create(
        title=task.title,
        details=task.details,
        deadline=task.deadline,
        user = task.user
    )

    return taskdb