#!/bin/bash

source ./venv/bin/activate

pytest test_app.py
TEST_RESULT=$?

deactivate

if [ $TEST_RESULT -eq 0 ]; then
  echo " All tests passed!"
  exit 0
else
  echo " Some tests failed."
  exit 1
fi

