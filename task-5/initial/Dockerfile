#FROM openjdk:24-slim
# 8080
FROM openjdk:26-ea-jdk
WORKDIR .
COPY build/libs/*.jar app.jar
ENTRYPOINT ["java","-jar","/app.jar"]