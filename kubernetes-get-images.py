from kubernetes import client, config
from kubernetes.client.models import V1Pod
from tabulate import tabulate


config.load_kube_config()

v1 = client.CoreV1Api()


def get_pods_for_all_namespaces() -> list:
    return v1.list_pod_for_all_namespaces().items


def get_images_from_pod(pod: V1Pod) -> list:
    return [ container.image for container in pod.spec.containers]
   
def  add_to_table(pod: V1Pod, images: str, table: list):
    table.append([pod.metadata.name, images])

def list_to_comma_string(images: list) -> str:
    return ', '.join(images)

TABLE_HEADERS = ["Pod", "Image"]
def main():
    table = []
    for pod in get_pods_for_all_namespaces():
        images = list_to_comma_string(get_images_from_pod(pod))
        add_to_table(pod, images, table)
    print(tabulate(table, headers=TABLE_HEADERS, tablefmt="simple_grid"))

if __name__ == "__main__":
    main()
