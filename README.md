# Compiling Kivy project to APK file.

## Step 1: Setting up Windows Subsystem for Linux (Windows Users ONLY)
#### Install Windows Subsystem for Linux (WSL) [Link](https://learn.microsoft.com/en-us/windows/wsl/install-manual)
Ensure powershell is running as administrator and run the below commands
- [x] `dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart`
- [x] `dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart`
- [x] Now restart your computer for the effects to take place (installing the wsl)

#### Download the Linux kernel update package
The Linux kernel update package installs the most recent version of the WSL 2 Linux kernel for running WSL inside the Windows operating system image.
- [x] [Download](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi) and install the latest package

Open powershell and run the below command (set WSL 2 as the default version when installing a new Linux distribution)
- [x] Run `wsl --set-default-version 2`
- [x] Open the [Microsoft Store](https://aka.ms/wslstore) and select your favorite Linux distribution.

## Step 2: Getting started with your current working directory on your pc, and wsl
#### Create your current working directory (cwd)
- [x] You want to create your cwd near the root folder of your pc. For example `c/Users/<yourname>/Documents/cwd`
Change `<yourname>` with your `pc name` or `username`, and cwd with your `project_folder_name`, where all your code will be hosted.

#### Open your Linux Distribution from the Applications
1. If your Linux Distribution was Debian, go to Start/Windows Key, then run Debian, if it was Ubuntu, go to Start/Windows Key then run Ubuntu.
2. A terminal will open. Set your username and your password.
3. Now you will navigate from your wsl terminal to your cwd in your pc.</br>
   3.1 Copy the path of your current working directory. Should look something like this `c/Users/<yourname>/Documents/cwd`.</br>
   3.2 On your wsl terminal, write the following code **`cd/mnt/c/Users/<yourname>/Documents/cwd`**. Remember to adjust to fit your cwd, and username or pc name.</br>
4. Good Progress!
## Step 3: Installing buildozer and its dependencies [Link](https://buildozer.readthedocs.io/en/latest/installation.html)
#### Install buildozer
Run your Linux Distribution again from Windows Applications (Windows Key > Linux Distribution)
- [x] Run `pip3 install --user --upgrade buildozer`, if error, run `sudo apt update`, enter password and click Enter.
- [x] Then run `sudo apt install python3-pip`, type `y` when prompted and click Enter.
- [x] Then rerun `pip3 install --user --upgrade buildozer`

Great Progress!!

#### install buildozer dependencies
From the documentation, you are required to run the following codes line by line:
      
      sudo apt update
      sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
      pip3 install --user --upgrade Cython==0.29.33 virtualenv  # the --user should be removed if you do this in a venv
      
      # add the following line at the end of your ~/.bashrc file
      export PATH=$PATH:~/.local/bin/

But we have already executed the firt line of code `sudo apt update`, so we do not need to repeat the task!

We now execute each of the remaining codes.
- [x] `sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev`
- [x] `pip3 install --user --upgrade Cython==0.29.33 virtualenv`
- [x] `export PATH=$PATH:~/.local/bin/`

## Step 4: Android Debug Bridge (adb)
adb is a powerful tool for debugging applications installed on your Android device that allows you to communicate with Android devices connected to your computer. It acts as a bridge between your development machine and the Android system on your device, enabling various functionalities for debugging and development purposes.

We will install adb on wsl terminal and check version, and also download it from internet then unzip it, then check version in powershell. The two versions must match in order for it to work properly.

That is, the version in wsl terminal must be the same version as the one installed manually and extracted and opened in powershell.

If you execute adb --version on your wsl, you will get error since it is not installed. We then install it on wsl.

Run the following on wsl.
- [x] `sudo apt install adb`
If prompted password, enter your password, if prompted to accept, type `y` then press Enter.
- [x] run `adb --version` to check the version on wsl

We now go to internet to [Download SDK Platform-Tools for Windows](https://developer.android.com/tools/releases/platform-tools#downloads) manually.

Extract only `adb application`, `AdbWinApi.dll application extention` and `AdbWinUsbApi.dll application extention`. The rest we do not need them.

Cut Paste the 3 files onto your current working directory.

Open file explorer where all your project code is saved, hold Shift Key + Right Click Mouse to open pop-up window. Scroll and select `Open Powershell window here`

Run the below commands in Powershell
- [x] adb --version

Take note of the version and compare if it is the same with wsl. (I will assume so since both have been installed the same day). If not, downgrade one, or upgrade one.

#### Open your Android phone
Go to
* Settings > About phone > Search for build number
* Tap build number 7 times to enable developer mode.
* Navigate back to Settings again.
* Go to Additional Information > Developer options or just search Developer options (Dependent with Android)
* Turn on `USB Debugging`

#### Initialize Buildozer
Run the following commands
- [x] `buildozer init` this initializes the SPEC file.

Navigate to your SPEC file. If you can't see it, run `nano buildozer.spec` or `nv buildozer.spec` or `vim buildozer.spec`.

It is recommended to refresh your project directory so that you can see it and open it on your Editor.

Inside the SPEC file, make sure to change
1. title of your app
2. package.name of your app
3. requirements = requirements = python3,kivy==2.3.0 *be very specific here and include versions of packages*
4. Click Save file

#### Turn on Android Debug Bridge
On your powershell, run
1. ./adb start-server
2. ./adb devices - *this should detect your android device since you turned on USB Debugging*

Good Progress so far!!

## Step 5: Compile Kivy project to Android
#### Sorting Permissions in wsl
Run the following code in wsl
- [x] `sudo mount -t drvfs C: /mnt/c -o metadata` and enter your password - *this gets rids of permission errors*

#### Compiling code to APK
Run the following code on wsl
- [x] `buildozer -v android debug`

## Congrats!
- [x] On your file explorer, you should be able to spot your phone, which you connected with your laptop via USB Debugging.
- [x] Save your apk file to the destination of your choice.

Click install.




