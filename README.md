# DeployFlow

Flask app -> GitHub Actions (tests + security scans) -> Docker Hub -> Argo CD -> Kubernetes.

## Local
    pip install -r requirements-dev.txt && pytest
    docker compose up --build      # http://localhost:5005

## Pipeline (.github/workflows/ci-cd.yml)
1. pytest, Bandit (SAST), Gitleaks (secrets), Trivy fs (deps + k8s misconfig)
2. Build image, Trivy image scan - HIGH/CRITICAL fails the build
3. Push `avan0/deployflow:<sha>` to Docker Hub
4. CI commits the new sha into `k8s/kustomization.yaml`
5. Argo CD detects the git change and syncs the cluster

## Argo CD setup
    kubectl create namespace argocd
    kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
    # repoURL already set in argocd/application.yaml
    kubectl apply -f argocd/application.yaml
    kubectl port-forward svc/argocd-server -n argocd 8081:443
    kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d

Repo setting needed: Settings -> Actions -> Workflow permissions -> Read and write.
