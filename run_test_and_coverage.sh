#!/usr/bin/env bash
coverage run -m game_runner game pytest
coverage report -m
coverage html 
