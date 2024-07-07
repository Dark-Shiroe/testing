d64Box

Mod box using glibc mebabo, main script box64droid and mobox files.

• Install glibc and wine 9.9
> curl -o install https://raw.githubusercontent.com/Dark-Shiroe/testing/main/install && chmod +x install && ./install


• If want to use wine 9.11 run cmd in termux
> cd ..
> rm -rf usr/glibc/opt/wine
> wget -q --show-progress https://github.com/Dark-Shiroe/testing/releases/download/boxfartbox/wine9.11.tar.xz
> tar -xf wine9.11.tar.xz -C $PREFIX/glibc/opt
> rm -rf wine9.11.tar.xz
> cd
