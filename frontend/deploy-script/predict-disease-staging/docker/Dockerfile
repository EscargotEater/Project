FROM node:12.20.0-alpine

ENV APP_ROOT /app

RUN mkdir ${APP_ROOT}

WORKDIR ${APP_ROOT}

COPY package.json ${APP_ROOT}

COPY package-lock.json ${APP_ROOT}

RUN npm install --ignore-platform

COPY . ${APP_ROOT}

# RUN yarn global add pm2 --prefix /usr/local

RUN npm run build

# ENTRYPOINT pm2 start ${APP_ROOT}/dist/main.js --name=deploy-docgen-pdf-service
ENTRYPOINT npm run start
