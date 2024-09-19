#!/bin/bash

minikube start

kubectl create ns argo
kubectl create ns argo-events

helm repo add argo https://argoproj.github.io/argo-helm
helm repo update

helm install argo-events argo/argo-events -n argo-events
helm install argo-workflows argo/argo-workflows -f values.yaml -n argo