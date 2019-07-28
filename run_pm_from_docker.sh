#!/bin/bash

docker run \
    -v /home/lukas/work/test/airflow/out:/mnt/data \
    tst_airflow \
    papermill \
        /project/notebooks/test_parametrization.ipynb \
        /mnt/data/test_parametrization_docker_manual.ipynb \
        -p timestamp 2017-07-26 \
        -p msg "Running manually from docker!"

