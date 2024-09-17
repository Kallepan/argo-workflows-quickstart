#!/bin/bash

minikube start

export ARGO_WORKFLOWS_VERSION=v3.5.10
kubectl create namespace argo
kubectl apply -n argo -f "https://github.com/argoproj/argo-workflows/releases/download/${ARGO_WORKFLOWS_VERSION}/quick-start-minimal.yaml"
