# login to azure
az login --use-device-code
# set subscription of assignment
az account set --subscription b7d6f930-14a3-47ba-9cbc-c8ca1bf77ce0
# create resource group and cluster
az group create --location centralus --name aks-rg
az aks create --resource-group aks-rg --name aks-ms --node-count 2 --generate-ssh-keys
#enable aad in order to enable rbac
az aks update --resource-group aks-rg --name aks-ms --enable-aad
az aks update --resource-group aks-rg --name aks-ms --enable-azure-rbac
# validate rbac was enabled
az aks show --resource-group aks-rg --name aks-ms --query "enableRbac"
# get credentials for kubectl
az aks get-credentials --resource-group aks-rg --name aks-ms
# use cluster context
kubectl config use-context aks-ms
# apply ingress controller 
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml
# verify it's running and check IP
kubectl get pods -n ingress-nginx
kubectl get svc -n ingress-nginx
# log in to docker
docker login
# build and push images
cd src\\service-a
docker build -t service-a .
docker tag service-a lioraft/service-a
docker push lioraft/service-a
cd ..\\service-b
docker build -t service-b .
docker tag service-b lioraft/service-b
docker push lioraft/service-b
cd ..\\..
# apply ingress
kubectl apply -f src\\ingress\\ingress.yaml
# prevent service a from "talking" to service b
kubectl apply -f src\\policy\\network-policy.yaml
# apply services
kubectl apply -f src\\service-a\\service-a-deployment.yaml
kubectl apply -f src\\service-b\\service-b-deployment.yaml
# check pods status
kubectl get pods


# reapply images after updating
kubectl set image deployment/service-a service-a=lioraft/service-a
kubectl set image deployment/service-b service-b=lioraft/service-b
