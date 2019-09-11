# flask-echo

Simple, "dockerized" Flask echo app, with Elastic's [apm-agent](https://www.elastic.co/guide/en/apm/get-started/current/agents.html) included.

# To Build

```
docker build --no-cache --force-rm -f Dockerfile -t flask-echo:v1.apm .
```

# Example Usage

```
docker run -d --name flask-echo \
              -e ELASTIC_APM_SERVICE_NAME=flask-echo \
              -e ELASTIC_APM_SERVER_URL=http://192.168.122.16:8200 \
              --network=host flask-echo:v1.apm
```
