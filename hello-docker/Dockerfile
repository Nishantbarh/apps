FROM openjdk:8-jdk-alpine as build
WORKDIR /app
COPY mvnw .
COPY .mvn .mvn
COPY pom.xml .
RUN  ./mvnw dependency:go-offline -B && chmod +x mvnw
COPY src src
RUN  ./mvnw package -DskipTests
RUN mkdir -p target/dependency && (cd target/dependency; jar -xf ../*.jar)

FROM openjdk:8-jre-alpine

ARG DEPENDENCY=/app/target/dependency
COPY --from=build ${DEPENDENCY}/BOOT-INF/lib /app/lib
COPY --from=build ${DEPENDENCY}/META-INF /app/META-INF
COPY --from=build ${DEPENDENCY}/BOOT-INF/classes /app
VOLUME /tmp
ENV JAVA_OPTS=""
ENTRYPOINT ["java","-cp","app:app/lib/*","com.example.howtodoinjava.hellodocker.HelloDockerApplication"]
