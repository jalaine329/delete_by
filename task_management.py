import time

# function to check for ongoing tasks of a specific type
def has_ongoing_task(es, task_type):
    tasks = es.tasks.list(actions=task_type)
    return any(task for task in tasks.get('nodes', {}).values() if task.get('tasks'))

# wait for ongoing tasks to complete
def wait_for_task_completion(es, task_type):
    while has_ongoing_task(es, task_type):
        print(f"Waiting for ongoing {task_type} to complete...")
        time.sleep(60) # wait for 60 seconds before checking again

# general function for polling task status
def poll_task_status(es, task_id):
    while True:
        task_response = es.tasks.get(task_id=task_id)
        if task_response.get('completed', False):
            break
        print(f"Waiting for {task_id} to complete...")
        time.sleep(60) # wait for 60 sec before checking again
