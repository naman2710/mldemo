# Deployment Architecture

We have a microservices architecture deployed on Azure using Docker containers. The CI/CD pipeline is managed by GitHub Actions, which builds and pushes Docker images to GitHub Container Registry. Kubernetes is used for orchestrating the containers. Configuration management is handled by Ansible, and infrastructure provisioning is done using Terraform.
