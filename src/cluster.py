import pulumi
import pulumi_kubernetes as k8s


config = pulumi.Config()
kubeconfig = config.get("kubeconfig")
provider = k8s.Provider("k8s-provider", kubeconfig=kubeconfig)

pulumi.export("kubeconfig", kubeconfig)
