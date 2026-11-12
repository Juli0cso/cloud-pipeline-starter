#!/usr/bin/env bash
set -euo pipefail
# Execute manually after reviewing on a NEW Ubuntu 24.04 EC2 lab instance.
sudo apt-get update
sudo apt-get install -y docker.io curl
sudo systemctl enable --now docker
sudo usermod -aG docker "$USER"
echo 'Docker installed. Log out and back in for group membership to take effect.'
echo 'WARNING: docker group membership provides root-equivalent privileges.'
