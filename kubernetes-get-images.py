from kubernetes import client, config

config.load_kube_config()

v1 = client.CoreV1Api()


def get_pods_for_all_namespaces() -> list:
    return v1.list_pod_for_all_namespaces().items

if __name__ == "__main__":
    pods = get_pods_for_all_namespaces()
    for pod in pods:
        print(pod.metadata.name)