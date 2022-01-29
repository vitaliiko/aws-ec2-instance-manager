FROM node:17.3.0-slim

WORKDIR serverless

RUN npm install -g serverless@2.70.0 \
	&& npm install serverless-python-requirements@5.3.0

RUN apt-get update \
	&& apt-get install --no-install-recommends -y python3.9 python3-pip \
	&& rm -rf /var/lib/apt/lists/*

COPY serverless-config/src .
COPY serverless-config/requirements.txt .
COPY serverless-config/serverless.yml .
