#!/usr/bin/env bash
#pytest && coverage run --branch --source game.py game_runner.py game_test.py && coverage report -m && coverage html
pytest && coverage run --branch game.py game_runner.py game_test.py && coverage report -m && coverage html