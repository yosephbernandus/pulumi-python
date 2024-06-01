"""A Kubernetes Python Pulumi program"""

# import pulumi
# import pulumi_kubernetes as k8s
# from pulumi_kubernetes.apps.v1 import Deployment, DeploymentSpecArgs
# from pulumi_kubernetes.meta.v1 import LabelSelectorArgs, ObjectMetaArgs
# from pulumi_kubernetes.core.v1 import ContainerArgs, PodSpecArgs, PodTemplateSpecArgs
#
# app_labels = { "app": "nginx" }
#
# config = pulumi.Config()
# kubeconfig = config.get("kubeconfig")
# provider = k8s.Provider("k8s-provider", kubeconfig=kubeconfig)
#
# deployment = Deployment(
#     "nginx",
#     spec=DeploymentSpecArgs(
#         selector=LabelSelectorArgs(match_labels=app_labels),
#         replicas=1,
#         template=PodTemplateSpecArgs(
#             metadata=ObjectMetaArgs(labels=app_labels),
#             spec=PodSpecArgs(containers=[ContainerArgs(name="nginx", image="nginx")])
#         ),
#     ),
#     opts=pulumi.ResourceOptions(provider=provider)
# )
#
# pulumi.export("name", deployment.metadata["name"])
#
#

from src import namespace
from src import database
