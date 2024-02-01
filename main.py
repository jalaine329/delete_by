from modules.es_client import select_cluster, init_es_client
from modules.task_management import wait_for_task_completion
from modules.doc_management import index_contains_docs, delete_docs, force_merge
from modules.config import clusters, filebeat_alias

def main():
    selected_cluster_name, cluster_urls = select_cluster(clusters)
    es = init_es_client(cluster_urls)
    indices = list(es.indices.get_alias(name=filebeat_alias).keys())

    # process each index    
    for index in indices:
        if index_contains_docs(es, index):
            wait_for_task_completion(es, "indices:data/write/delete/byquery")
            wait_for_task_completion(es, "indices:admin/forcemerge*")
            delete_docs(es, index)
            wait_for_task_completion(es, "indices:data/write/delete/byquery")
            wait_for_task_completion(es, "indices:admin/forcemerge*")
            force_merge(es, index) 
        else:
            print(f"No matching documents found in {index}, skipping delete and force merge.")

if __name__ == "__main__":
    main()
