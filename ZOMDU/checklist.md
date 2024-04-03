# IoT Project ZOMDU Checklist

This is the checklist outlining what we should have accomplished during the two hands-on experiments.

## Overview
- [ ] understand concept of the system
- [ ] understand concept of Docker and Containerization
- [ ] understand concept of Kubernetes and Rancher

## Set up MQTT Broker  on Raspberry Pi
- [ ] connect to Wi-Fi
- [ ] install docker
- [ ] run EMQX (map port 1883 and 18083)
- [ ] manage MQTT broker via port 18083
- [ ] test MQTT service using client program
- [ ] run Producer image to publish data to MQTT broker
- [ ] run Subscriber image to see the published messages

## Set up Database
- [ ] login to Rancher
- [ ] deploy InfluxDB with your namespace (map port 8086)
- [ ] configure the user information (you'll need this information for accessing to the database from other service)
- [ ] configure DNS by using ingress in load balancing on Rancher

## Deploy Consumer on Raspberry Pi
- [ ] run Consumer image for listening the data on the subscribed topics and put the data into InfluxDB
- [ ] keep running until the database has some data for analysis

## Apply Machine Learning Model to Collected Data
- [ ] load data from InfluxDB using InfluxDB client library
- [ ] train the model
- [ ] cross validation (hyperparameter tuning)
- [ ] test the accuracy of model
- [ ] apply your model for real-time prediction
- [ ] put the output of model in the database
- [ ] containerize and deploy on Rancher

## (Option I) Deploy Command Center on Raspberry Pi
- [ ] run Command Center image to periodically poll the output value from analytical part and publish to the MQTT broker
- [ ] see the subscriber

## (Option II) Visualize the output using Grafana
- [ ] deploy Grafana on Rancher
- [ ] add InfluxDB as a datasource
- [ ] create dashboard
