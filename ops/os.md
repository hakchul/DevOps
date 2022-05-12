<!-- markdownlint-disable MD033 -->

# OS

> Instllations and Settings

## Ubuntu

### User Management

> https://help.ubuntu.com/lts/serverguide/user-management.html

* Adding and Deleting Users

    ```bash
    # adding a user
    sudo adduser {user}
    # add a user to a group
    sudo adduser {user} {group}
    # temporarily lock a user account
    sudo passwd -l {user}
    # unlock a user account
    sudo passwd -u {user}
    # delete a user
    sudo deluser {user}
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
    sudo apt-get install openssh-server
    ```

* Setting Example (/etc/ssh/sshd_config)

    ```conf
    PermitRootLogin no
    PasswordAuthentication no
    ```

* Restart service

    ```bash
    sudo service ssh restart
    ```

### SSH Client

* Using public key

    ```bash
    # generate public/private key
    ssh-keygen
    # copy public key to server
    ssh-copy-id {user}@{server.ip} -p {port}
    ```

* Turn off checking known_host

    ```bash
    ssh -o StrictHostKeyChecking=no {user}@{host}
    ```

### Firewall

> https://help.ubuntu.com/community/UFW

* UFW - Uncomplicated Firewall

    ```bash
    # allow specific ip address with subnet
    sudo ufw allow from 192.168.0.0/16
    # limit ssh
    sudo ufw limit ssh
    # enable ufw
    sudo ufw enable
    # status
    sudo ufw status
    sudo ufw status numbered
    # delete
    # sudo ufw delete limit ssh
    # sudo ufw delete 1
    ```

### Samba Server

* Install samba server

    ```bash
    sudo apt-get install samba
    ```

* Add below on /etc/samba/smb.conf

    ```conf
    [shared]
        comment = Samba
        path = {/path/to/share}
        force user = {user}
        read only = no
        writable = yes
        browsable = yes
        guest ok = yes
        create mask = 0664
        directory mask = 0775
    ```

* Restart service

    ```bash
    sudo service smbd restart
    ```


### DLNA Server

* Install DLNA server

    ```bash
    sudo apt-get install minidlna
    ```

* Add below on /etc/minidlna.conf

    ```conf
    media_dir=A,/home/{user}/Music
    media_dir=P,/home/{user}/Pictures
    media_dir=V,/home/{user}/Videos
    db_dir=/var/cache/minidlna          # Needs to be un-commented
    log_dir=/var/log                    # Needs to be un-commented
    ```

* Restart service

    ```bash
    sudo service minidlna restart
    ```

### Reverse SSH

* Reverse SSH

    ```bash
    # on host server
    ssh -T -R {bind_port}:localhost:{host_port} {user}@{relay.server.ip} -p {port}
    ssh -T -R 9999:localhost:22 {user}@100.100.100.100 -p 2222
    # on relay server
    ssh {host_user}@localhost -p {bind_port}
    ssh {user}@localhost -p 9999
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
    # create new swap file
    sudo dd if=/dev/zero of=/swapfile bs=1G count=16
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

### Ubuntu tracker

* Modify ignored-directires

    ```bash
    gsettings set org.freedesktop.Tracker.Miner.Files ignored-directories "['po', 'CVS', 'core-dumps', 'lost+found', 'data', 'venv']"
    tracker reset -r
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

### Power Management

* Sleep Status

    ```bash
    systemctl status sleep.target suspend.target hibernate.target hybrid-sleep.target
    ```

* Disable Sleep

    ```bash
    sudo systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target
    ```

* Enable Sleep

    ```bash
    sudo systemctl unmask sleep.target suspend.target hibernate.target hybrid-sleep.target
    ```

### Partitioning

* Parted

    ```bash
    # list block device
    lsblk
    # run parted
    sudo parted
    # (parted) select device
    select /dev/sda
    # (parted) display selected
    print
    # (parted) make label
    mklabel msdos
    # (parted) make partition
    mkpart primary 1MB 100%
    # (parted) quit
    quit
    # format partition
    sudo mkfs.ext4 /dev/sda1
    ```

### Language

* Install Languages

    ```bash
    sudo apt install language-pack-en language-pack-en-base
    sudo apt install language-pack-ko language-pack-ko-base
    sudo update-locale LANG=en_US.utf8 # reboot required
    ```

### Compression

* Split tar
    ```bash
    # create and break archive file into small blocks each of size 1GB
    tar cvf - {PATH_FILE} | split -b 1G - "filename.tar.part"
    # extract split files
    cat filename.tar.part* | tar xvf -
    ```

### Troubleshooting

* Mouse wheel jumping

    ```bash
    sudo apt install imwheel
    imwheel --kill --buttons "4 5"
    ```
