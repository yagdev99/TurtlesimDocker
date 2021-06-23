# ROS Turtlesim GUI using Docker

## What is Docker?
Docker is a tool which is enables us run an application in an isolated enviroment called container. Containers are lightweight and contain all dependencies required to run a particular application which frees us from the hassel of manual installation of dependencies. Containers can be easily be shared as they are independent of host operating system. Shared containers work exactly the same on every machine with Docker installed.



## Running Turtlesim ROS Node on Docker

1) Install Docker from [here](https://docs.docker.com/engine/install/)
2) Check if Docker properly install by running in Docker Terminal: \
```docker run hello-world```
3) Now run: \
```sudo docker run --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" --name roslocal -it ros:melodic /bin/bash``` 
This step will take some time so be patient and ensure internet connectivity. 


    | Option     | Description|
    |------------|------------|
    |`--net=host` | Connects the container to host network|
    |`--env="DISPLAY"` | Passes enviroment variable which enables us to use GUI|
    |`--volume`| Allows us to mount volume from local storage from host machine|
    |`--name roslocal`| Allows us to give `roslocal` as name of thecontainer. If not specified Docker gives a random name to it. Check using `docker ps -a`|
    |`-it`| Allows us to use interactive mode |
    |`ros:melodic`| Name of the Docker Image. See more [here](https://hub.docker.com/_/ros)
    | `/bin/bash` | To get bash shell in the terminal|

4) To open another terminal of same instance of `roslocal` container, run: \
    ```
    $ docker exec -it roslocal bash
    ```
5) 




## Resources
1. To learn more about Docker refer to [Docker Docs](https://docs.docker.com/get-started/overview/)
2. Docker vs. Virtual Machines: https://geekflare.com/docker-vs-virtual-machine/
3. Writing DockerFile: https://docs.docker.com/engine/reference/builder/
