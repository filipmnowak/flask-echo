# flask-echo

Simple, "dockerized" Flask echo app

## Build

```sh
export FLASK_ECHO_REPO='flask-repo'
export FLASK_ECHO_VERSION='v0.1a'
sudo docker build --rm --no-cache -f Dockerfile -t ${FLASK_ECHO_REPO}:${FLASK_REPO_VERSION} .
```

## Run

```sh
sudo docker run --rm -d -p 8080:8080 ${FLASK_ECHO_REPO}:${FLASK_REPO_VERSION}
```
