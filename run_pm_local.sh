#!/bin/bash

papermill \
    ./notebooks/test_parametrization.ipynb \
    ./out/test_parametrization_manual.ipynb \
    -p timestamp 2017-07-26 \
    -p msg "Running manually on local!"

