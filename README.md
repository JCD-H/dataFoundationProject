Useful Commands:

spin up the docker services
docker-compose -f kafka_docker_compose.yml up -d

connect to the container
docker exec -it kafka /bin/sh 

create a topic
/bin/kafka-topics --create --replication-factor 1 --partitions 1 --topic first_topic --bootstrap-server localhost:29092

list topics 
/bin/kafka-topics --list --bootstrap-server localhost:29092

Consume topics
/bin/kafka-console-consumer --bootstrap-server localhost:29092 --topic first_topic --from-beginning

Produce topics
/bin/kafka-console-producer --broker-list localhost:29092 --topic first_topic


Useful Links:

https://medium.com/@thomasjay200/kafka-with-docker-2023-8381669e7768
