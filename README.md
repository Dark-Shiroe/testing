d64Box

Mod box using glibc mebabo, main script box64droid and mobox files.

• Install glibc and wine 9.11
> curl -o install https://raw.githubusercontent.com/Dark-Shiroe/testing/main/install && chmod +x install && ./install


• If you want to use wine 9.9 run this command in termux
```
cd ..
```
```
rm -rf usr/glibc/opt/wine
```
```
wget -q --show-progress https://github.com/Dark-Shiroe/testing/releases/download/boxfartbox/wine.tar.xz
```
```
tar -xf wine.tar.xz -C $PREFIX/glibc/opt
```
```
rm -rf wine.tar.xz
```
```
cd
```

![Screenshot_2024-07-10-20-08-15-070_com termux](https://github.com/Dark-Shiroe/testing/assets/68985198/2a935fc1-0b4e-4535-89c5-47d2e38daecc)
