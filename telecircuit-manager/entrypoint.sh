#!/usr/bin/env bash

set -e

function install_node_modules {
    echo "Installing node modules."
    npm install
    echo "Node modules has been installed"
}

function run_webpack {
    echo "Running webpack."
    npm run build
}

function main {
    install_node_modules
    run_webpack
}

main