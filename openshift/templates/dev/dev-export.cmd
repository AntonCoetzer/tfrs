oc export secret -o json -n mem-tfrs-dev > dev-secret.json
oc export configmap -o json -n mem-tfrs-dev > dev-configmap.json
oc export rolebinding -o json -n mem-tfrs-dev > dev-rolebinding.json
oc export pvc -o json -n mem-tfrs-dev > dev-storage.json
oc export bc -o json -n mem-tfrs-dev > dev-build-config.json
oc export dc -o json -n mem-tfrs-dev > dev-deployment-config.json
oc export service -o json -n mem-tfrs-dev > dev-service.json
oc export route -o json -n mem-tfrs-dev > dev-route.json
