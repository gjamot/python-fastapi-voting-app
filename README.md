# python-fastapi-voting-app

## 🔁 Build & push Docker images vers ECR
```bash
# Exemple pour le frontend
aws ecr get-login-password | docker login --username AWS --password-stdin <ECR_URL>
docker build -t react-frontend ./frontend
docker-compose up --build
docker tag react-frontend:latest <ECR_URL>/react-frontend:latest
docker push <ECR_URL>/react-frontend:latest
```

---

## 🌐 Accès Web
- React : via ALB
- FastAPI : via ALB (ou API Gateway)
- PostgreSQL : via RDS (accès privé)

---

Tu peux maintenant exécuter :
```bash
cd terraform
terraform init
terraform apply
```