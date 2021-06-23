# ROS Turtlesim GUI using Docker

## What is Docker?
Docker is a tool that enables us to run an application in an isolated environment called a container. Containers are lightweight and contain all dependencies required to run a particular application which frees us from the hassle of manual installation of dependencies. Containers can be easily be shared as they are independent of the host operating system. Shared containers work exactly the same on every machine with Docker installed.



## Running Turtlesim ROS Node on Docker

1) Install Docker from [here](https://docs.docker.com/engine/install/)
2) Check if Docker properly install by running in Docker Terminal: \
```
$ docker run hello-world
```
3) Now run: 
```
$ sudo docker run --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" --name roslocal -it ros:melodic /bin/bash
``` 
This step will take some time so be patient and ensure internet connectivity. 


| Option     | Description|
|------------|------------|
|`--net=host` | Connects the container to host network|
|`--env="DISPLAY"` | Passes environment variable which enables us to use GUI|
|`--volume`| Allows us to mount a volume from local storage from the host machine|
|`--name roslocal`| Allows us to give `roslocal` as the name of the container. If not specified Docker gives a random name to it. Check using `docker ps -a`|
|`-it`| Allows us to use interactive mode |
|`ros:melodic`| Name of the Docker Image. See more [here](https://hub.docker.com/_/ros)
| `/bin/bash` | To get bash shell in the terminal|

4) Installing Turtlesim: 

    First update the container using
    ```
    $ apt-get update
    ```


    
    To install Turtlesim run:
    ```
    $ sudo apt-get install ros-melodic-turtlesim
    ```

5) To open another terminal for the same instance of `roslocal` container, run: 
    ```
    $ docker exec -it roslocal bash
    ```
    For every terminal you open make sure to source:
    ```
    $ source /opt/ros/melodic/setup.bash
    ```
    
7) To start ROS Master run:
    ```
    $ roscore
    ```

    To start turtlesim node run:

    ```
    $ rosrun turtlesim turtlesim_node
    ```

    To start turtlesim tele-operation run:
    ```
    $ rosrun turtlesim turtle_teleop_key
    ```




## Resources
1. To learn more about Docker refer to [Docker Docs](https://docs.docker.com/get-started/overview/)
2. Docker vs. Virtual Machines: https://geekflare.com/docker-vs-virtual-machine/
3. Writing DockerFile: https://docs.docker.com/engine/reference/builder/
