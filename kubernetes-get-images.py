from kubernetes import client, config

config.load_kube_config()

v1 = client.CoreV1Api()


def get_pods_for_all_namespaces() -> list:
    return v1.list_pod_for_all_namespaces().items


def get_images_from_pod(pod) -> list:
    images = []
    for container in pod.spec.containers:
        images.append(container.image)
    return images 

def main():
    for pod in get_pods_for_all_namespaces():
        print(f"Container name: {pod.metadata.name} | images: {get_images_from_pod(pod)}")

if __name__ == "__main__":
    main()
