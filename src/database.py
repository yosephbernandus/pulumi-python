import pulumi
import pulumi_kubernetes as k8s

from . import cluster

k8s.helm.v3.Chart(
    release_name="redis",
    config=k8s.helm.v3.ChartOpts(
        chart="redis",
        namespace="database",
        repo="bitnami",
        version="19.5.0",
        values={
            "architecture": "standalone",
            "auth": {"enabled": False, "sentinel": False},
            "master": {"persistence": {"enabled": False}},
            "usePassword": False,
        },
    ),
    opts=pulumi.ResourceOptions(provider=cluster.provider),
)


k8s.core.v1.PersistentVolumeClaim(
    resource_name="postgres-pvc",
    metadata=k8s.meta.v1.ObjectMetaArgs(
        name="postgres-pvc",
        namespace="database",
        annotations={"pulumi.com/skipAwait": "true"},
    ),
    spec=k8s.core.v1.PersistentVolumeClaimSpecArgs(
        access_modes=["ReadWriteOnce"],
        resources=k8s.core.v1.VolumeResourceRequirementsArgs(
            requests={"storage": "8Gi"}
        ),
    ),
    opts=pulumi.ResourceOptions(provider=cluster.provider),
)
