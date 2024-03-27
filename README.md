# IoT-Final-Project
This is a guideline for students who enroll in 2102541 IoT Fundamental Course (academic year 2023)

Class Instructors:

- Assoc. Prof. Chaodit Aswakul (https://ee.eng.chula.ac.th/chaodit-aswakul/)
- Assoc. Prof. Wanchalerm Pora (https://ee.eng.chula.ac.th/wanchalerm-pora/)

Department of Electrical Engineering, Faculty of Engineering, Chulalongkorn University, Thailand

This repository was created by Patchapong Kulthumrongkul 6670165121@student.chula.ac.th

## System Architecture
![Alt text](/Diagram.svg)

The primary objectives of this project include designing and implementing a full-stack IoT system and deploying all services to run in a real operating environment. Therefore, collaboration with teammates is essential to develop a comprehensive system, utilizing GitHub as our workspace for development.

### System components
- **ESP32** 
  - ESP32 collects the data from attached sensors and publish the data to a sensor gateway via MQTT.
  - ESP32 receives the command by subscribing the topic that is used to send command from other services and send the command to the actuators.

- **Raspberry Pi (Sensor Gateway)**
  - **MQTT Broker**
    - The broker facilitates communication among IoT devices within the local area network (Wi-Fi) 
  **Note:** ESP32 boards and Raspberry Pi must connect to the same Wi-Fi network to be within the same local area network (LAN).
    - For the EMQX MQTT broker (ref: https://www.emqx.io/), you can configure the broker through port 18083, while the common MQTT port is 1883.
  - **Consumer**
    - Python script listens to messages published to the broker and writes that data into an InfluxDB database.
    - If you wish to provide real-time streaming data to the analytics component, you can accomplish this directly here as well.
  - **Command Center**
    - If your analytics service controls actuators, you can utilize the Command Center to poll action data from the database and publish commands to the MQTT broker.
  - **Docker Container**
    - All services operating on the Raspberry Pi must run as Docker images, necessitating the containerization of all applications within the Raspberry Pi.
- **IoT Cloud Serve** 
  - **InfluxDB**
    - InfluxDB is a time-series database designed for collecting streaming data from IoT sensors.
    - InfluxDB is running on port 8086.
    - You can read and write data using InfluxDB client library. (ref: https://docs.influxdata.com/influxdb/v1/tools/api_client_libraries/)
  - **Data Analytics**
    - After you have collected data from IoT devices, you can leverage that data to derive more meaningful insights.
    - You can develop regression or classification models to predict outputs by learning from the collected data.
    - Once your model is prepared for prediction, utilize real-time data fed from the Consumer to perform real-time predictions.
  - **Website UI** (optional)
    - You can utilize the InfluxDB UI for visualization without needing to implement anything
    - Additionally, you can employ other visualization services such as Grafana.
    - Alternatively, you have the option to design your own simple web application using both backend and frontend technologies.
  - **Docker Container & Rancher**
    - All services operating on the cloud must run as Docker images, necessitating the containerization of all applications within the laptop.
    - Once you have obtained the images, you will need to deploy them on Rancher, a management platform for Kubernetes clusters.
    - Additionally, you'll need to map the services to the outside world using Domain Name System (DNS).
  
**Noted that all of your source code must be pushed to your group's public GitHub repository.**