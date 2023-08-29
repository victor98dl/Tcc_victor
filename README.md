# Tutorial para reprodução do framework para detectção de ataques DDoS em redes SDN utilizando aprendizado de máquina em microsserviços

## Requisitos
- Ubuntu 22.04 LTS ou superior;
- 
- Cluster kubernetes (pode ser via kind, minikube, kubeadm) - tutorial Kubeadm (https://gitlab.com/gercom-ufpa/openran/oran-onos/-/blob/84976baf6660e2d65bbf55271daed697ba27752d/docs/kubernetesInstall.md);

## Preparo cluster

- helm repo add metallb https://metallb.github.io/metallb;
- helm install metallb metallb/metallb -n metallb-system --create-namespace;
-  nano ipaddresspool.yaml
   piVersion: metallb.io/v1beta1
    kind: IPAddressPool
    metadata:
        name: ip-pool
        namespace: metallb-system
    spec:
        addresses:
        10.126.1.140/32
- nano l2config.yaml
    apiVersion: metallb.io/v1beta1
    kind: L2Advertisement
      metadata:
        name: l2config
      namespace: metallb-system
    spec:
        ipAddressPools:
            ip-pool
    nodeSelectors:
      matchLabels:
            kubernetes.io/hostname: oranufpa

## Implementação para testes
- git clone https://github.com/victor98dl/Tcc_victor.git
- cd Tcc_victor/Kubernetes
- kubectl create namespace classificador
- kubectl apply -f deployment.yaml -n classificador
- kubectl apply -f service.yaml -n classificador
- kubectl get service -o wide -n classificador
- classificador-svc   NodePort   10.101.7.241   <none>        5000:30000/TCP   3m20s   app=classificador
- helm install onos-classic -n onos-classic --set atomix.podAntiAffinity.enabled=false --set podAntiAffinity.enabled=false --set replicas=1 --set atomix.replicas=1 --set image.repository=muriloavlis/oran-onos --set image.tag=latest --set atomix.persistence.enabled=false  --set atomix.image.tag=3.1.12 onosproject/onos-classic --create-namespace
- kubectl apply -f onos-service.yaml -n onos-classic
- kubectl get svc -n onos-classic
-  http://10.126.1.140:31396/onos/ui/#/topo2
