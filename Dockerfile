FROM node:alpine

WORKDIR /usr/src/app

RUN npm install -g serverless@2.44.0 && \
  npm install --save-dev serverless-localstack

# Install python/pip
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install awscli
RUN pip install awscli-local

RUN apk add wget unzip && rm -rf /var/cache/apk/*

WORKDIR /usr/src/app
RUN wget -O sls-examples https://github.com/serverless/examples/archive/refs/heads/master.zip \ 
  && unzip ./sls-examples && rm ./sls-examples

COPY --from=golang:1.13-alpine /usr/local/go/ /usr/local/go/
ENV PATH="/usr/local/go/bin:${PATH}"

COPY . .

# sls deploy --verbose -s $STAGE

CMD ["tail", "-f", "/dev/null"]