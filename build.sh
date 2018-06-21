#!/usr/bin/env bash

set -e

function install_docker {
    apt-get update
    echo "Installing docker..."
    curl -fsSL get.docker.com -o get-docker.sh
    sh get-docker.sh
    rm get-docker.sh
    echo "Docker installed"
}

function install_docker_compose {
    echo "Installing docker-compose..."
    curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose
    echo "$(docker-compose --version)"
}

function main {
    install_docker
    install_docker_compose
}

main