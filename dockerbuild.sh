#!/bin/sh
docker build -t jubalhershaw/devhausrepo .
docker run --name wftest jubalhershaw/devhausrepo