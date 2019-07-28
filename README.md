# Test airflow papermill docker

Purpose of this repo is to test airflow with papermill and docker integration (and maybe kubernetes in the future)

Some files:
- `Dockerfile` describes simple image with jupter server and papermill
- `docker-compose.yml` contains build instructions, run `$ docker-compose build` to build the image
- `run_pm_from_docker.sh` then runs the papermill built image 
- `run_pm_local.sh` run papermill locally

Directories:
- `out/` - dir for papermill to output notebooks; contains some examples
- `home/` - airflow home, contains dags
- `notebooks/` - dir with input notebooks for papermill
