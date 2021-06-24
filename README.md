# ROS Turtlesim GUI using Docker

## What is Docker?
Docker is a tool that enables us to run an application in an isolated environment called a container. Containers are lightweight and contain all dependencies required to run a particular application which frees us from the hassle of manual installation of dependencies. Containers can be easily be shared as they are independent of the host operating system. Shared containers work exactly the same on every machine with Docker installed.


## Running ROS on Docker using Docker Image
1) Install Docker from [here](https://docs.docker.com/engine/install/)

2) Check if Docker properly install by running in Docker Terminal: 
    ```
    docker run hello-world
    ```

3) To pull [Turtlesim Docker Image](https://hub.docker.com/r/yagneshde/ros_turtlesim) run:

    ```
    docker pull yagneshde/ros_turtlesim:latest
    ```
4) To run the Docker Image run:
    ```
    docker images
    docker run -it <IMAGE ID> 
    ```

5) To create catkin workspace follow Step 6 of Running Turtlesim ROS Node on Docker (Manually)



## Running Turtlesim ROS Node on Docker (Manually)

1) Install Docker from [here](https://docs.docker.com/engine/install/)
2) Check if Docker properly install by running in Docker Terminal: 
    ```
    docker run hello-world
    ```
3) Now run: 

    ```
    docker run --net=host --env="DISPLAY" -v "${PWD}:/myvol" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" --name roslocal -it ros:melodic /bin/bash
    ``` 
This step will take some time so be patient and ensure internet connectivity.




| Option     | Description|
|------------|------------|
|`--net=host` | Connects the container to host network|
|`--env="DISPLAY"` | Passes environment variable which enables us to use GUI|
|`-v "${PWD}:/myvol"`|Mounts the current working directory of host machine at the time of starting the container. To access current working directory in the container navigate to myvol. Note: Make sure the name of the folder is unique, i.e. `myvol` should not clash with other folders in the container's root directory.|
|`--volume`| Allows us to mount a volume from local storage from the host machine|
|`--name roslocal`| Allows us to give `roslocal` as the name of the container. If not specified Docker gives a random name to it. Check using `docker ps -a`|
|`-it`| Allows us to use interactive mode |
|`ros:melodic`| Name of the Docker Image. See more [here](https://hub.docker.com/_/ros)
| `/bin/bash` | To get bash shell in the terminal|

* Note: 
    * To stop the Docker container use:

        ``` shell
        docker ps 
        docker stop <CONTAINER ID>
        ```


    * To start Docker container use:
        ```shell
        docker ps -a
        docker start <CONTAINER ID>
        docker exec -it <CONTAINER NAME> bash
        ```
        

4) Installing Turtlesim: 

    First update the container using
    ```
    apt-get update
    ```
    
    To install Turtlesim run:
    ```
    sudo apt-get install ros-melodic-turtlesim
    ```

5) To open another terminal for the same instance of `roslocal` container, run: 
    ```
    docker exec -it roslocal bash
    ```

6) Creating catkin workspace:
    ```shell
    cd myvol
    mkdir -p ~/catkin_ws/src
    cd catkin_ws
    catkin_make
    ```

    Creating ROS package named `ros_basics`
    ```shell
    cd src
    catkin_create_pkg ros_basics
    ```

7) To source setup.bash open a new terminal of same instance of the container from step 5.
    ```shell
    sudo apt update
    sudo apt install vim -y
    cd
    vim .bashrc
    ```

    Now navigate to the bottom of the file and add the following:
    ```shell
    source /opt/ros/melodic/setup.bash
    source /myvol/catkin_ws/devel/setup.bash
    ```

    Press ESC and type `:wq` to save and exit vim.
    
8) To start ROS Master run:
    ```shell
    roscore
    ```

    To start turtlesim node run:

    ```shell
    rosrun turtlesim turtlesim_node
    ```

    To start turtlesim tele-operation run:
    ```shell
    rosrun turtlesim turtle_teleop_key
    ```

## Running ROS Publisher and Subscriber Nodes
1) Clone the package into the created catkin workspace,`catkin_ws`
    ```shell
    cd /myvol/catkin_ws/src
    git clone https://github.com/yagdev99/TurtlesimDocker
    cd ..
    catkin_make
    ```
2) Starting ROS Master:
    ```
    roscore
    ```
3) To run `talker.py` open a new terminal of the same instance of the container and run:
    ```
    rosrun TurtlesimDocker talker.py
    ```

4) To run `listener.py` open a new terminal of the same instance of the container and run:
    ```
    rosrun TurtlesimDocker listener.py
    ```
You should now see messages being puslished by `talker.py` and displayed by `listener.py`


## Resources
1. To learn more about Docker refer to [Docker Docs](https://docs.docker.com/get-started/overview/)
2. Docker vs. Virtual Machines: https://geekflare.com/docker-vs-virtual-machine/
3. Writing DockerFile: https://docs.docker.com/engine/reference/builder/
