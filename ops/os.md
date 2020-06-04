<!-- markdownlint-disable MD033 -->

# OS

> Instllations and Settings

## Ubuntu 18.04

### User Management

> https://help.ubuntu.com/lts/serverguide/user-management.html

* Adding and Deleting Users

    ```bash
    # adding a user
    sudo adduser {user}
    # temporarily lock or unlock a user account
    sudo passwd -l {user}
    sudo passwd -u {user}
    # delete a user
    sudo deluser {user}
    # add a user to a group
    sudo adduser {user} {group}
    # change password
    sudo passwd
    ```

* Enable/Disable the root account password

    ```bash
    # enable
    sudo passwd
    # disable
    sudo passwd -l root
    ```

### SSH Server

* Install

    ```bash
    apt-get install openssh-server
    ```

* Settings (/etc/ssh/sshd_config)

    ```conf
    PermitRootLogin no
    PasswordAuthentication no
    ```

    ```bash
    # restart service
    sudo service ssh restart
    ```

### SSH Client

* Using public key

    ```bash
    ssh-keygen    # generate public/private key
    ssh-copy-id {user}@{server.ip} -p {port} # copy public key  to server
    ```

* Turn off checking known_host

    ```bash
    ssh -o StrictHostKeyChecking=no {user}@{host}
    ```

### Reverse SSH

* Reverse SSH

    ```bash
    # on host server
    ssh -T -R {bind_port}:localhost:{host_port} {user}@{relay.server.ip} -p {port}
    ssh -T -R 9999:localhost:22 hc@100.100.100.100 -p 2222
    # on relay server
    ssh {host_user}@localhost -p {bind_port}
    ssh hc@localhost -p 9999
    ```

### FTP Server

* Install

    ```bash
    sudo apt-get install vsftpd
    ```

* Settings (/etc/vsftpd.conf)

    ```conf
    write_enable=YES
    utf8_filesystem=YES
    ```

    ```bash
    # restart service
    sudo service vsftpd restart
    ```

### Swapfile

* Change swap size

    ```bash
    # disable the swap file and delete it
    sudo swapoff /swapfile
    sudo rm  /swapfile
    # create new swap file
    sudo dd if=/dev/zero of=/swapfile bs=1M count=8192
    # set the swap file permissions to 600
    sudo chmod 600 /swapfile
    # format the file as swap
    sudo mkswap /swapfile
    # enable use of swap file
    sudo swapon /swapfile
    ```

    > https://askubuntu.com/a/1075516

### File Systems

* exFAT

    ```bash
    sudo apt-get install exfat-fuse exfat-utils
    ```

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

### Etc

* bash-completion

    ```bash
    sudo apt install bash-completion
    ```

* upgrade

    ```bash
    sudo apt update
    sudo apt upgrade
    ```

### Security

* Disable Ctrl+Alt+Delete

    ```bash
    sudo systemctl mask ctrl-alt-del.target
    sudo systemctl daemon-reload
    ```

    > https://help.ubuntu.com/lts/serverguide/console-security.html

### System Time

* Fix Time Differences in Ubuntu & Windows Dual Boot

    ```bash
    # use rtc time in the local time zone
    timedatectl set-local-rtc 1 --adjust-system-clock
    ```

### Lock and black screen

* Set timeout of "Blank Screen"

    **GUI:**

    Settings → Power → Power Saving → Blank screen

    **Terminal:**

    ```bash
    gsettings set org.gnome.desktop.session idle-delay 3600 # an hour
    ```

* Set timeout of "Lock screen after blank"

    **GUI:**

    Settings → Privacy → Screen Lock → Lock screen after blank for

    **Terminal:**

    ```bash
    gsettings set org.gnome.desktop.screensaver lock-delay 60 # a minute
    ```

### Language

* Install Languages (terminal)

    ```bash
    sudo apt install language-pack-en language-pack-en-base
    sudo apt install language-pack-ko language-pack-ko-base
    sudo update-locale LANG=en_US.utf8 # reboot required
    ```

  * Keyboard > layout > Korean (101/104 key compatible)
  * Language Support > keyboard input method system > iBus
  * iBus Preferences > Input Method > Add > Korean - Hangul # re-login required

* Install Languages (GUI)

    1. Open **Settings > Region & Language**

        <img src="assets/region_language.png" width="80%">

    2. Click **Manage Installed languages**

        <img src="assets/language_support.png" width="50%">

    3. Click **Install / Remove Languages...**

    4. Check **Korean**

        <img src="assets/installed_languages.png" width="50%">

    5. Apply

    6. Add **Korean (Hangul)** to **Input Sources**

        > If it is does not appear, restart ubuntu

        <img src="assets/input_sources_hangul.png" width="80%">

* Korean Hangul/Hanja keys

    1. Open **Ubuntu Software**

    2. Install **GNOME Tweaks**

        <img src="assets/install_tweaks.png" width="80%">

    3. Open **GNOME Tweaks > Keyboard & Mouse**

        <img src="assets/tweaks.png" width="80%">

    4. Click "Additional Layout Options"

        <img src="assets/additional_layout.png" width="50%">

    5. Check **Right Alt as Hangul, right Ctrl as Hanja**

### Troubleshooting

* Mouse wheel jumping

    ```bash
    sudo apt install imwheel
    imwheel --kill --buttons "4 5"
    ```
