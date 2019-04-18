# OS

## Ubuntu 18.04

### System time

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

### Hangul

* Add Korean

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
