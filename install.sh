#!/bin/bash

echo "Installing termux-am"
pkg install termux-am -y &>/dev/null

termux-setup-storage & sleep 4 &>/dev/null

while true; do
    if [ -d ~/storage/shared ]; then
        break
    else
        echo "Storage permission denied"
    fi
    sleep 3
done

echo "Installing termux packages"
apt-get clean
apt-get update >/dev/null 2>&1
apt-get -y --with-new-pkgs -o Dpkg::Options::="--force-confdef" upgrade >/dev/null 2>&1
pkg install x11-repo -y &>/dev/null
pkg install pulseaudio -y &>/dev/null
pkg install xwayland -y &>/dev/null
pkg install wget -y &>/dev/null
pkg install tsu -y &>/dev/null
pkg install root-repo -y &>/dev/null
pkg install patchelf -y &>/dev/null
pkg install p7zip -y &>/dev/null
pkg install xorg-xrandr -y &>/dev/null
pkg install ncurses-utils -y &>/dev/null
pkg install hashdeep -y &>/dev/null
pkg install termux-x11-nightly -y &>/dev/null
pkg install python nmap vulkan-tools -y &>/dev/null
pkg install git python -y &>/dev/null
pkg install coreutils -y &>/dev/null
pkg install socat -y &>/dev/null
pip install objgraph &>/dev/null
pip install aiofiles &>/dev/null
pip install blessings &>/dev/null

echo "Installing BoxFartBox"
wget https://github.com/mebabo1/menano/releases/download/Box/box64.tar.xz
tar xf box64.tar.xz
rm -rf box64.tar.xz
wget https://github.com/Dark-Shiroe/testing/releases/download/boxfartbox/optboxfartbox.tar.xz
tar xf optboxfartbox.tar.xz
rm -rf optboxfartbox.tar.xz
wget https://github.com/Dark-Shiroe/testing/releases/download/boxfartbox/etcfonts.tar.gz
tar xf etcfonts.tar.gz
rm -rf etcfonts.tar.gz
wget https://github.com/Dark-Shiroe/testing/releases/download/boxfartbox/sharefont.tar.gz
tar xf sharefont.tar.gz
rm -rf sharefont.tar.gz
wget https://github.com/Dark-Shiroe/testing/releases/download/boxfartbox/locale.7z
7z x locale.7z -o$PREFIX/glibc/lib/locale
rm -rf locale.7z
mv opt/wine usr/glibc/opt
rm -rf opt
rm -rf root
wget https://raw.githubusercontent.com/Dark-Shiroe/testing/main/boxfartbox &>/dev/null
wget https://raw.githubusercontent.com/Dark-Shiroe/testing/main/boxfartbox.py &>/dev/null
wget https://raw.githubusercontent.com/Dark-Shiroe/testing/main/start-fartbox.py &>/dev/null
wget https://raw.githubusercontent.com/Dark-Shiroe/testing/main/winetricks &>/dev/null
chmod +x box64droid winetricks
mv box64droid box64droid.py start-box64.py winetricks $PREFIX/bin

echo "To start BoxFartBox run 'boxfartbox --start'"
