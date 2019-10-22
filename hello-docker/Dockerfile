FROM openjdk:8-jdk-alpine
WORKDIR /app
COPY mvnw  .
COPY .mvn  .mvn
COPY pom.xml  .
RUN ./mvnw dependency:go-offilne -B
COPY src src
RUN ./mvnw package -DSkipTests
RUN mkdir -p target/dependency && (cd target/dependecy; jar -xf ../*.jar)

FROM openjdk:8-jre-alpine

ARG DEPENDENCY=/app/target/dependency
COPY --from=build ${DEPENDENCY}/BOOT_INF/lib /app/lib
COPY --from=build ${DEPENDENCY}/META_INF  /app/META_INF
COPY --from=build ${DEPENDENCY}/BOOT_INF/classes  /app
VOLUME /tmp
ENV JAVA_OPTS=""
ENTRYPOINT ["java","-cp","app:app/lib/*","com.example.howtodoinjava.HelloDockerApplication"]
