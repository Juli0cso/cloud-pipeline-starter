#!/usr/bin/env bash
set -euo pipefail
IMAGE="${1:?Provide image name as first argument}"
# Classroom version: image package must be PUBLIC in GHCR for anonymous docker pull.
case "$IMAGE" in ghcr.io/*:*) ;; *) echo "Invalid image reference" >&2; exit 1;; esac
docker volume create cloud-tasks-data >/dev/null
docker pull "$IMAGE"
# Make sure that port 80 is not occupied by a host web server.
docker rm -f cloud-tasks-api >/dev/null 2>&1 || true
docker run -d --name cloud-tasks-api --restart unless-stopped   -p 80:8000 -v cloud-tasks-data:/data   -e DB_PATH=/data/tasks.db "$IMAGE"
for i in $(seq 1 20); do
  if curl --fail --silent http://127.0.0.1/health >/dev/null; then
    echo "Deploy succeeded: $IMAGE"
    exit 0
  fi
  sleep 2
done
docker logs cloud-tasks-api >&2
exit 1
