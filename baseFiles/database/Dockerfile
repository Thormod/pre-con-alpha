FROM mysql:5

ENV MYSQL_ROOT_PASSWORD 123  
ENV MYSQL_DATABASE app_db  
ENV MYSQL_USER app_db_user  
ENV MYSQL_PASSWORD 123

ADD setup.sql /docker-entrypoint-initdb.d  