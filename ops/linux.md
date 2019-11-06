# LINUX

> Commands

## Commands

### Mount Drivers

* Mount volume on boot

  * Check uuid

    ```bash
    sudo blkid
    ```

  * Edit /etc/fstab

    ```config
    UUID={UUID} {/PATH/TO/MOUNT} {TYPE} defaults,nofail 0 0
    ```

### SSH

* Turn off checking known_host

    ```bash
    ssh -o StrictHostKeyChecking=no {user}@{host}
    ```

* Reverse SSH

    ```bash
    # on host server
    ssh -T -R {bind_port}:localhost:{host_port} {user}@{relay.server.ip} -p {port}
    ssh -T -R 9999:localhost:22 hc@100.100.100.100 -p 2222
    # on relay server
    ssh {host_user}@localhost -p {bind_port}
    ssh hc@localhost -p 9999
    ```
