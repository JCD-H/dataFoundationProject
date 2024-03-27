Useful Commands:

spin up the docker services
docker-compose -f docker-compose.yml up -d

connect to the container
docker exec -it kafka /bin/sh 
docker exec -it [image_id] /bin/sh 

docker exec -it 5d1192d7c08e /bin/sh 

create a topic
/bin/kafka-topics --create --replication-factor 1 --partitions 1 --topic test_topic --bootstrap-server localhost:29092

list topics 
/bin/kafka-topics --list --bootstrap-server localhost:29092

Consume topics
/bin/kafka-console-consumer --bootstrap-server localhost:29092 --topic test_topic --from-beginning

Produce topics
/bin/kafka-console-producer --broker-list localhost:29092 --topic first_topic

spin down containers - stops and deletes them I believe
docker-compose -f docker-compose.yml down

activate my virtual env on windows
dataFoundationVenv\scripts\activate

start the flink container
docker run --name flink -p 8081:8081 -p 6123:6123 flink_with_python /bin/bash -c "jobmanager.sh start-foreground && taskmanager.sh start-foreground"


Useful Links:

https://medium.com/@thomasjay200/kafka-with-docker-2023-8381669e7768
