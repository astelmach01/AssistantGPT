#!/bin/bash

install.sh

poetry install --with dev

pre-commit install
