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
    mkdir ~/venv
    # python2
    virtualenv --system-site-packages -p python2.7 ~/venv/py2
    # python3
    virtualenv --system-site-packages -p python3 ~/venv/py3
    ```

* Activate the virtual environment

    ```bash
    # python2
    source py2/bin/activate
    # python3
    source py3/bin/activate
    ```

* Alias (Optional)

    ```bash
    # add aliases in ~/.bashrc file
    alias venv_py2='source ~/venv/py2/bin/activate'
    alias venv_py3='source ~/venv/py3/bin/activate'
    ```