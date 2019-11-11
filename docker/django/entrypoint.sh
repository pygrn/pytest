#!/usr/bin/env bash
set -e

DOCKER_USER=www-data

exec /usr/sbin/gosu "$DOCKER_USER" "$@"
