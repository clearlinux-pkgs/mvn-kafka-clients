PKG_NAME := mvn-kafka-clients
URL = https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/2.0.0/kafka-clients-2.0.0.jar
ARCHIVES = https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/2.0.0/kafka-clients-2.0.0.pom : https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/0.8.2.1/kafka-clients-0.8.2.1.jar : https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/0.8.2.1/kafka-clients-0.8.2.1.pom : 

include ../common/Makefile.common
