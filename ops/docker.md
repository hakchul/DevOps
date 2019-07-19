# Docker

## Ubuntu

* Installation
    
    ```bash
    sudo apt install docker.io
    sudo usermod -aG docker $USER   # add user to docker group
    ```

## Windows

* Connect SSH into the Docker VM (MobyLinuxVM) on Windows

    ```bash
    docker run --net=host --ipc=host --uts=host --pid=host -it --privileged ^
        --security-opt=seccomp=unconfined --rm -v /:/host debian /bin/sh
    ```
