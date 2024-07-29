# Docker

## Ubuntu

* Installation

    ```bash
    sudo apt install docker.io
    sudo usermod -aG docker $USER
    # Log out and log back in
    ```

* Attach X11 Server
    ```bash
    docker run -it --rm -v '/tmp/.X11-unix:/tmp/.X11-unix' -e DISPLAY=$DISPLAY ubuntu
    ```

* Attach USB Device
    ```bash
    docker run -it --rm --device /dev/bus/usb ubuntu
    ```

## Windows

* Connect SSH into the Docker VM (MobyLinuxVM) on Windows

    ```bash
    docker run --net=host --ipc=host --uts=host --pid=host -it --privileged ^
        --security-opt=seccomp=unconfined --rm -v /:/host debian /bin/sh
    ```
