# Redis Cache

Redis is a popular in-memory key-value store that can be used as a caching solution. Redis supports a variety of data structures, including strings, hashes, lists, sets, and sorted sets. It also offers advanced features like pub/sub messaging and Lua scripting. Redis is designed to be fast, reliable, and scalable, making it a popular choice for high-traffic applications.

## Advantages:
* Redis is extremely fast and can handle a large number of requests per second.
* Redis can be used as both a caching solution and a database.
* Redis is highly scalable, making it suitable for applications that require high availability.
* Redis supports various data structures, making it flexible and easy to use.

## Disadvantages:
* Redis is an in-memory caching solution, which means that it requires a significant amount of memory to function effectively.
* Redis does not provide automatic data replication, so it is up to the user to ensure data consistency and availability.
* Redis is not suitable for applications that require persistent storage.

## Setup instructions

#### 1. Installation
    pip install redis 
    or,
    brew install redis

#### 2. Defining External Routes from the API
#### 3. run redis-server
    redis-server
#### 4. run `python service.py` to make the service active
#### 5. run `python redisConnector.py` to see the response
