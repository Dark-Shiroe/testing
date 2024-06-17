import os, time, shutil, sys, subprocess
ver=200524
def start_boxfartbox():
    os.system("clear")
    if "LD_PRELOAD" in os.environ:
        del os.environ["LD_PRELOAD"]
    print("Starting Termux-X11...")
    os.system("termux-x11 :0 &>/dev/null &")
    print("Starting PulseAudio...")
    subprocess.run(["pulseaudio", "--start", "--load=module-native-protocol-tcp auth-ip-acl=127.0.0.1 auth-anonymous=1", "--exit-idle-time=-1"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
    os.system('tar -xf $PREFIX/glibc/opt/libs/wineesync/disable.tar.gz -C "/sdcard/BoxFartBox"')
    os.system('WINEDLLOVERRIDES="mscoree=" box64 wine wineboot &>/dev/null')
    os.system("rm $HOME/.wine/dosdevices/z: && rm $HOME/.wine/dosdevices/d: &>/dev/null")
    os.system("cp -r $PREFIX/glibc/opt/Scripts/dosdevices $HOME/.wine")
    os.system('cp -r $PREFIX/glibc/opt/prefix/start/* "$HOME/.wine/drive_c/ProgramData/Microsoft/Windows/Start Menu"')
    print("Installing Stuff...")
    os.system('box64 wine regedit "$PREFIX/glibc/opt/prefix/tweak.reg" &>/dev/null')
    os.system("tar -xf $PREFIX/glibc/opt/prefix/fix-fonts.tar.xz -C $HOME/.wine/drive_c/windows")
    os.system('box64 wine "$PREFIX/glibc/opt/prefix/tweak.bat" &>/dev/null')
    os.system('cp -r $PREFIX/glibc/opt/box64.box64rc "/sdcard/BoxFartBox"')
    os.system('cp -r $PREFIX/glibc/opt/box86.box86rc "/sdcard/BoxFartBox"')
    os.system('cp -r $PREFIX/glibc/opt/libs/turnip-zink/turnip.conf "/sdcard/BoxFartBox"')
    os.system('tar -xf $PREFIX/glibc/opt/libs/locale/en.tar.gz -C "/sdcard/BoxFartBox"')
    os.system('tar -xf $PREFIX/glibc/opt/libs/wineesync/enable.tar.gz -C "/sdcard/BoxFartBox"')
    print("Done!")
    main_menu()
def fonts_glibc():
    os.system("clear")
    print("Downloading JP fonts...")
    os.system("wget -q --show-progress https://github.com/Dark-Shiroe/mefartbox/releases/download/mefartbox/fonts.tar.xz")
    print("Extracting font to glibc/share...")
    os.system('tar -xJf "$HOME/fonts.tar.xz" -C /data/data/com.termux/files/usr/glibc/share')
    os.system('rm -rf "$HOME/fonts.tar.xz"')
    os.system('mv /data/data/com.termux/files/usr/glibc/share/Fonts /data/data/com.termux/files/usr/glibc/share/fonts')
    print("Done...")
    main_menu()
def sett_menu():
    os.system("clear")
    print("Setting Config!")
    print("")
    print("Select to start:")
    print("1) Change Local")
    print("2) Change Turnip")
    print("3) Change WineEsync")
    print("4) Install Fonts Jp(glibc)")
    print("5) Change Cpu Core Boost")
    print("6) Back to previous menu")
    print("")
    choice = input()
    if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7":
        print("Incorrect or empty option!")
        sett_menu()
    elif choice == "1":
        def change_local():
            os.system("clear")
            file = open("/sdcard/BoxFartBox/locale.conf", "r")
            content = file.readline()[21:]
            print("Current:", content)
            file.close()
            print("")
            print("Select Local language:")
            print("1) English (en_US)")
            print("2) Japan (ja_JP)")
            print("3) Korean (ko_KR)")
            print("4) Back to previous menu")
            print("")
            choice = input()
            if choice != "1" and choice != "2" and choice != "3" and choice != "4":
                print("Incorrect or empty option!")
                change_local()
            elif choice == "4":
                sett_menu()
            else:
                os.system("clear")
                if choice == "1":
                    file = open("/sdcard/BoxFartBox/locale.conf", "w")
                    file.write('os.environ["LC_ALL"]="en_US.UTF8"')
                    file.close()
                elif choice == "2":
                    file = open("/sdcard/BoxFartBox/locale.conf", "w")
                    file.write('os.environ["LC_ALL"]="ja_JP.UTF8"')
                    file.close()
                elif choice == "3":
                    file = open("/sdcard/BoxFartBox/locale.conf", "w")
                    file.write('os.environ["LC_ALL"]="ko_KR.UTF8"')
                    file.close()
                change_local()
        change_local()
    elif choice == "2":
        def change_turnip():
            os.system("clear")
            file = open("/sdcard/BoxFartBox/turnip.conf", "r")
            content = file.readline()[2:]
            print("Current:", content)
            file.close()
            print("")
            print("Select Turnip version:")
            print("1) Default (glibc)")
            print("2) Airidosas")
            print("3) Mobox")
            print("4) Back to previous menu")
            print("")
            choice = input()
            if choice != "1" and choice != "2" and choice != "3" and choice != "4":
                print("Incorrect or empty option!")
                change_turnip()
            elif choice == "4":
                sett_menu()
            else:
                os.system("clear")
                if choice == "1":
                    os.system('cp -r $PREFIX/glibc/opt/libs/turnip-zink/turnip.conf "/sdcard/BoxFartBox"')
                elif choice == "2":
                    os.system('cp -r $PREFIX/glibc/opt/libs/turnip-zink/airidosas/turnip.conf "/sdcard/BoxFartBox"')
                elif choice == "3":
                    os.system('cp -r $PREFIX/glibc/opt/libs/turnip-zink/mobox/turnip.conf "/sdcard/BoxFartBox"')
                change_turnip()
        change_turnip()
    elif choice == "3":
        def change_wineesync():
            os.system("clear")
            file = open("/sdcard/BoxFartBox/wineesync.conf", "r")
            content = file.readline()[1:]
            print("Current:", content)
            file.close()
            print("")
            print("Select WineEsync mode:")
            print("1) Enable")
            print("2) Disable")
            print("3) Back to previous menu")
            print("")
            choice = input()
            if choice != "1" and choice != "2" and choice != "3":
                print("Incorrect or empty option!")
                change_wineesync()
            elif choice == "3":
                sett_menu()
            else:
                os.system("clear")
                if choice == "1":
                    os.system('tar -xf $PREFIX/glibc/opt/libs/wineesync/enable.tar.gz -C "/sdcard/BoxFartBox"')
                elif choice == "2":
                    os.system('tar -xf $PREFIX/glibc/opt/libs/wineesync/disable.tar.gz -C "/sdcard/BoxFartBox"')
                change_wineesync()
        change_wineesync()
    elif choice == "4":
        os.system("clear")
        fonts_glibc()
    elif choice == "5":
        def change_cpucore():
            os.system("clear")
            print("")
            print("Select Cpu Core:")
            print("1) sd865 or over")
            print("2) sd865 or below")
            print("3) Back to previous menu")
            print("")
            choice = input()
            if choice != "1" and choice != "2" and choice != "3":
                print("Incorrect or empty option!")
                change_wineesync()
            elif choice == "3":
                sett_menu()
            else:
                os.system("clear")
                if choice == "1":
                    os.system('tar -xf $PREFIX/glibc/opt/libs/cpucore/sd865.tar.gz -C "$PREFIX/glibc/opt/Scripts"')
                elif choice == "2":
                    os.system('tar -xf $PREFIX/glibc/opt/libs/cpucore/sd864.tar.gz -C "$PREFIX/glibc/opt/Scripts"')
                sett_menu()
        change_cpucore()
    elif choice == "6":
        main_menu()
def uninstall():
    print("Uninstalling BoxFartBox...")
    glibc_path = "/data/data/com.termux/files/usr/glibc"
    wine_prefix_path ="/data/data/com.termux/files/home/.wine"
    shutil.rmtree(glibc_path)
    shutil.rmtree(wine_prefix_path)
def main_menu():
    start_boxfartbox()
    check_config()
    check_prefix()
    os.system("clear")
    print("BoxFartBox Menu!")
    print("")
    print("Select to start:")
    print("1) Run Wine")
    print("2) Run Wine (debug version)")
    print("3) Recreate Wine prefix")
    print("4) Update Box64")
    print("5) Setting")
    print("6) Exit")
    print("88) Uninstall BoxFartBox")
    print("")
    choice = input()
    if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7":
        print("Incorrect or empty option!")
        main_menu()
    elif choice == "1":
        os.system("python3 $PREFIX/glibc/opt/Scripts/b64-start.py")
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
            os.system("$PREFIX/glibc/bin/box64 wineserver -k &>/dev/null")
            main_menu()
        else:
            print(" Stopping Wine...")
            print("")
            os.system("$PREFIX/glibc/bin/box64 wineserver -k &>/dev/null")
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
        os.system("python3 $PREFIX/glibc/opt/Scripts/b64.py --s")
        exit()
    elif choice == "5":
        sett_menu()
    elif choice == "6":
        print("")
        print("Stopping Termux-X11...")
        print("")
        os.system('pkill -f "app_process / com.termux.x11"')
        os.system('pkill -f pulseaudio')
        exit()
    elif choice == "88":
        uninstall()
        
#def start():
    if len(sys.argv) < 2:
        print("Empty argument, use --help to see available arguments")
    elif sys.argv[1] == "--s":
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
    elif sys.argv[1] == "--reinstall":
        os.system("curl -o install https://raw.githubusercontent.com/Dark-Shiroe/testing/main/install && chmod +x install && ./install")
    elif sys.argv[1] == "--version":
        print("20.05.24")
    elif sys.argv[1] == "--help":
        print("BoxFartBox (native version) - configured tools to launch Box64, Box86, Wine 8.0, DXVK with Adreno GPU drivers in Termux")
        print("Usage: boxfartbox {argument}")
        print("Available arguments:")
        print("--s - start BoxFartBox")
        print("--uninstall - uninstall BoxFartBox (all data in prefix will be clear)")
        print("--reinstall - reinstall BoxFartBox (all data in prefix will be clear)")
        print("--version - show current version of Box64Droid")
        print("--help - see this menu and exit")
    else:
        print("Invalid argument, use --help to see available arguments")
        
if __name__ == "__main__":
    main_menu()
