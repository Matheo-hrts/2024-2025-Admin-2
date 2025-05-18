#/bin/bash

set -e

default_version="3"
version=${1:-"$default_version"}


docker build -t matheohrts/woody_misc_api:"$version" misc-api
docker tag matheohrts/woody_misc_api:"$version" matheohrts/woody_misc_api:latest

docker build -t matheohrts/woody_products_api:"$version" products-api
docker tag matheohrts/woody_products_api:"$version" matheohrts/woody_products_api:latest

docker build -t matheohrts/woody_orders_api:"$version" orders-api
docker tag matheohrts/woody_orders_api:"$version" matheohrts/woody_orders_api:latest

docker build -t matheohrts/woody_rp:"$version" reverse-proxy
docker tag matheohrts/woody_rp:"$version" matheohrts/woody_rp:latest

docker build -t matheohrts/woody_database:"$version" database
docker tag matheohrts/woody_database:"$version" matheohrts/woody_database:latest

docker build -t matheohrts/woody_front:"$version" front
docker tag matheohrts/woody_front:"$version" matheohrts/woody_front:latest

docker build -t matheohrts/woody_worker:"$version" rabbitmq
docker tag matheohrts/woody_worker:"$version" matheohrts/woody_worker:latest

# avec le "set -e" du début, je suis assuré que rien ne sera pushé si un seul build ne c'est pas bien passé

docker push matheohrts/woody_misc_api:"$version"
docker push matheohrts/woody_misc_api:latest

docker push matheohrts/woody_products_api:"$version"
docker push matheohrts/woody_products_api:latest

docker push matheohrts/woody_orders_api:"$version"
docker push matheohrts/woody_orders_api:latest

docker push matheohrts/woody_rp:"$version"
docker push matheohrts/woody_rp:latest

docker push matheohrts/woody_front:"$version"
docker push matheohrts/woody_front:latest

docker push matheohrts/woody_database:"$version"
docker push matheohrts/woody_database:latest

docker push matheohrts/woody_worker:"$version"
docker push matheohrts/woody_worker:latest
