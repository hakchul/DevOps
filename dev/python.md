# Python

## Virtualenv

* Installation

    ```bash
    # python2
    sudo pip install -U virtualenv     # system-wide install
    # python3
    sudo pip3 install -U virtualenv     # system-wide install
    ```

* Create a new virtual environment

    ```bash
    # python2
    virtualenv --system-site-packages -p python2.7 ./py2
    # python3
    virtualenv --system-site-packages -p python3 ./py3
    ```

* Activate the virtual environment

    ```bash
    # python2
    source py2/bin/activate
    # python3
    source py3/bin/activate
    ```
