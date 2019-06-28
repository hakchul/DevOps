# Docker

## Windows

* Connect SSH into the Docker VM (MobyLinuxVM) on Windows

    ```bash
    docker run --net=host --ipc=host --uts=host --pid=host -it --security-opt=seccomp=unconfined --privileged --rm -v /:/host debian /bin/sh
    ```
