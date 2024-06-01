import pulumi
import pulumi_kubernetes as k8s

from . import cluster

k8s.core.v1.Namespace(
    resource_name="test",
    metadata=k8s.meta.v1.ObjectMetaArgs(name="test", labels={"name": "test"}),
    opts=pulumi.ResourceOptions(provider=cluster.provider),
)
