import os, time, shutil, sys
ver=200524
def start_boxfartbox():
    os.system("clear")
    if "LD_PRELOAD" in os.environ:
        del os.environ["LD_PRELOAD"]
    print("Starting Termux-X11...")
    os.system("termux-x11 :0 &>/dev/null &")
    print("Starting PulseAudio...")
    os.system('pulseaudio --start --load="module-native-protocol-tcp auth-ip-acl=127.0.0.1 auth-anonymous=1" --exit-idle-time=-1 &>/dev/null')
def check_config():
    config_folder = "/sdcard/BoxFartBox/"
    box64droid_config = config_folder + "BoxFartBox.conf"
    dxvk_config = config_folder + "DXVK_D8VK.conf"
    dxvk_config_hud =  config_folder + "DXVK_D8VK_HUD.conf"
    print("Checking configuration...")
    if not os.path.exists(config_folder):
        os.mkdir(config_folder)
    if not os.path.exists(box64droid_config):
        shutil.copyfile("/data/data/com.termux/files/usr/glibc/opt/BoxFartBox.conf", box64droid_config)
    if not os.path.exists(dxvk_config):
        shutil.copyfile("/data/data/com.termux/files/usr/glibc/opt/DXVK_D8VK.conf", dxvk_config)
    if not os.path.exists(dxvk_config_hud):
        shutil.copyfile("/data/data/com.termux/files/usr/glibc/opt/DXVK_D8VK_HUD.conf", dxvk_config_hud)
    exec(open('/sdcard/BoxFartBox/BoxFartBox.conf').read())
    exec(open('/sdcard/BoxFartBox/DXVK_D8VK_HUD.conf').read())
def check_prefix():
    if not os.path.exists("/data/data/com.termux/files/home/.wine"):
        print("Wine prefix not found! Creating...")
        create_prefix()
def recreate_prefix():
    prefix_path="/data/data/com.termux/files/home/.wine"
    os.system("clear")
    print("Removing previous Wine prefix...")
    shutil.rmtree(prefix_path)
    print("Creating Wine prefix...")
    create_prefix()
def create_prefix():
    os.system('WINEDLLOVERRIDES="mscoree=" box64 wine wineboot &>/dev/null')
    os.system("rm $HOME/.wine/dosdevices/z: && rm $HOME/.wine/dosdevices/d: &>/dev/null")
    os.system("cp -r $PREFIX/glibc/opt/Scripts/dosdevices $HOME/.wine")
    os.system('cp -r $PREFIX/glibc/opt/prefix/start/* "$HOME/.wine/drive_c/ProgramData/Microsoft/Windows/Start Menu"')
    print("Installing Stuff...")
    os.system('box64 wine "$PREFIX/glibc/opt/prefix/OverrideDlls.bat" &>/dev/null && box64 wine "$PREFIX/glibc/opt/apps/install.bat" &>/dev/null')
    os.system('box64 wine regedit "$PREFIX/glibc/opt/prefix/one.reg" &>/dev/null')
    os.system("tar -xf $PREFIX/glibc/opt/prefix/fix-fonts.tar.xz -C $HOME/.wine/drive_c/windows")
    os.system('cp -r $PREFIX/glibc/opt/box64.box64rc "/sdcard/BoxFartBox"')
    os.system('cp -r $PREFIX/glibc/opt/box86.box86rc "/sdcard/BoxFartBox"')
    print("Done!")
    main_menu()
def fonts_glibc():
    os.system("clear")
    print("Downloading JP fonts...")
    os.system("wget -q --show-progress https://github.com/Dark-Shiroe/testing/releases/download/boxfartbox/fontsglibc.tar.xz")
    print("Extracting font to glibc/share...")
    os.system('tar -xJf "$HOME/fontsglibc.tar.xz" -C /data/data/com.termux/files/usr/glibc/share')
    print("Done...")
    main_menu()
def main_menu():
    os.system("clear")
    print("BoxFartBox Menu!")
    print("")
    print("Select to start:")
    print("1) Wine")
    print("2) Wine (debug version)")
    print("3) Recreate Wine prefix")
    print("4) Update Box64")
    print("5) Winetricks")
    print("6) Install Fonts Jp(glibc)")
    print("7) Exit")
    print("")
    choice = input()
    if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7":
        print("Incorrect or empty option!")
        main_menu()
    elif choice == "1":
        os.system("python3 $PREFIX/bin/start-fartbox.py")
        exit()
    elif choice == "2":
        os.system("clear")
        print("Wine will be started with debug info, log will be saved in /sdcard/boxfartbox.log")
        print("To exit from BoxFartBox press type '1' (or any key) or '2' to back to main menu then press Enter")
        os.system("BOX86_LOG=1 BOX86_SHOWSEGV=1 BOX86_DYNAREC_LOG=1 BOX86_DYNAREC_MISSING=1 BOX86_DLSYM_ERROR=1 BOX64_LOG=1 BOX64_SHOWSEGV=1 BOX64_DYNAREC_LOG=1 BOX64_DYNAREC_MISSING=1 BOX64_DLSYM_ERROR=1 WINEDEBUG=+err taskset -c 4-7 box64 wine explorer /desktop=shell,1152x600 $PREFIX/glibc/opt/7-Zip/7zFM >/sdcard/boxfartbox.log 2>&1 &")
        os.system("am start -n com.termux.x11/com.termux.x11.MainActivity &>/dev/null")
        stop = input()
        if stop == "2":
            print(" Stopping Wine...")
            os.system("box64 wineserver -k &>/dev/null")
            main_menu()
        else:
            print(" Stopping Wine...")
            print("")
            os.system("box64 wineserver -k &>/dev/null")
            print(" Stopping Termux-X11...")
            print("")
            os.system("pkill -f pulseaudio && pkill -f 'app_process / com.termux.x11'")
            print(" Exiting from Box64Droid...")
            print("")
            exit()
    elif choice == "3":
        recreate_prefix()
        create_prefix()
    elif choice == "4":
        os.system("clear")
        os.system("pkg install -y git; unset LD_PRELOAD; export GLIBC_PREFIX=/data/data/com.termux/files/usr/glibc; export PATH=$GLIBC_PREFIX/bin:$PATH; cd ~/; git clone https://github.com/ptitSeb/box64; cd ~/box64; sed -i 's/\/usr/\/data\/data\/com.termux\/files\/usr\/glibc/g' CMakeLists.txt; sed -i 's/\/etc/\/data\/data\/com.termux\/files\/usr\/glibc\/etc/g' CMakeLists.txt; mkdir build; cd build; cmake --install-prefix $PREFIX/glibc .. -DARM_DYNAREC=1 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DBAD_SIGNAL=ON -DSD845=ON; make -j8; make install; rm -rf ~/box64; cd ~/")
        os.system("python3 $PREFIX/bin/boxfartbox.py --start")
        exit()
    elif choice == "5":
        os.system("clear")
        print("Starting Winetricks... To back to main menu press Ctrl+c exit from Winetricks in Termux-X11")
        os.system("am start -n com.termux.x11/com.termux.x11.MainActivity &>/dev/null")
        os.system("box64 winetricks >/dev/null 2>&1")
        main_menu()
    elif choice == "6":
        os.system("clear")
        fonts_glibc()
    elif choice == "7":
        print("")
        print("Stopping Termux-X11...")
        print("")
        os.system('pkill -f "app_process / com.termux.x11"')
        os.system('pkill -f pulseaudio')
        exit()
def start():
    if len(sys.argv) < 2:
        print("Empty argument, use --help to see available arguments")
    elif sys.argv[1] == "--start":
        start_boxfartbox()
        check_config()
        check_prefix()
        main_menu()
    elif sys.argv[1] == "--uninstall":
        print("Uninstalling BoxFartBox...")
        glibc_path = "/data/data/com.termux/files/usr/glibc"
        wine_prefix_path ="/data/data/com.termux/files/home/.wine"
        shutil.rmtree(glibc_path)
        shutil.rmtree(wine_prefix_path)
        os.system("rm $PREFIX/bin/boxfartbox")
        os.system("rm $PREFIX/bin/boxfartbox.py")
        os.system("rm $PREFIX/bin/start-fartbox.py")
    elif sys.argv[1] == "--reinstall":
        os.system("curl -o install https://raw.githubusercontent.com/Dark-Shiroe/testing/main/install && chmod +x install && ./install")
    elif sys.argv[1] == "--version":
        print("20.05.24")
    elif sys.argv[1] == "--help":
        print("BoxFartBox (native version) - configured tools to launch Box64, Box86, Wine 8.0, DXVK with Adreno GPU drivers in Termux")
        print("Usage: boxfartbox {argument}")
        print("Available arguments:")
        print("--start - start BoxFartBox")
        print("--uninstall - uninstall BoxFartBox (all data in prefix will be clear)")
        print("--reinstall - reinstall BoxFartBox (all data in prefix will be clear)")
        print("--version - show current version of Box64Droid")
        print("--help - see this menu and exit")
    else:
        print("Invalid argument, use --help to see available arguments")
if __name__ == "__main__":
    start()
