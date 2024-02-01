from modules.task_management import poll_task_status

# function to check if an index contains documents to delete
# make changes to query based on which docs you are trying to remove from your index/cluster
# for most people the query section is going to have to change completely
def index_contains_docs(es, index):
    query = {
        "query": {
            "bool": {
                "must": [
                    {"term": {"<field>": "<value>"}}, 
                    {"wildcard": {"<field>": "<value>"}}
                ]
            }
        },
        "size": 0 # only interested in whether or not the docs exist, not in the actual docs
    }
    try:
        response = es.search(index=index, body=query)
        return response["hits"]["total"]["value"] > 0
    except Exception as e:
        print(f"Error checking documents in {index}: {e}")
        return False
    
# function to delete docs based on the specified criteria
# make changes to query based on which docs you are trying to remove from your index/cluster
# for most people the query section is going to have to change completely
def delete_docs(es, index):
    query = {
        "query": {
            "bool": {
                "must": [
                    {"term": {"<field>": "<value>"}},
                    {"wildcard": {"<field>": "<value>"}}
                ]
            }
        }
    }

    # submit the delete_by as a task and get task id
    try:
        response = es.delete_by_query(index=index, body=query, wait_for_completion=False)
        task_id = response['task']
        print(f"Delete_by task_id is {task_id}...")
        poll_task_status(es, task_id)
        print(f"Delete_by query on index: {index} completed")
    
    except Exception as e:
        print(f"Error deleting documents from {index}: {e}")

# function to force merge an alias (all underlying indices)
def force_merge(es, index):
    try:
        # submit the force merge as a task
        response = es.indices.forcemerge(index=index, only_expunge_deletes=True, wait_for_completion=False)
        task_id = response['task']
        print(f"Force merge on index: {index} completed")
        poll_task_status(es, task_id)
        print(f"Force merge on index: {index} complete")

    except Exception as e:
        print(f"Error force merging {index}: {e}")
