This project is about geospatial realestate api.
    - This api can POST or GET house information which will contain address, latitude, longitude, type, number of bed, number of bath.
  
Core Technologies used for this project
    - Python
    - Flask
    - Docker
    - SwaggerUi
    - Postgresql
    - AWS
    - Unittest
  
To start local environment
    - In terminal type: ./start_script.sh
    - In browser type: http://localhost:80
    - 
To stop local environment
    - In terminal type: ./stop_script.sh

For AWS access
    - In browser type: http://15.223.119.85
    - Try out API using SwaggerUi

Unittest
    Please run test.py for simple unittests

Time used for this project
    - Approximately 1 hour for environment setup including docker, database
    - Approximately 1.5 hour for coding
    - Approximately 45 minutes for SwaggerUi work including finding template and making yaml file
    - Approximately 30 minutes for unittest

Time used for AWS deployment
    - Approximately 1 hour and 15 minutes for deploying db(postgresql) and setting up ECR and ECS