# Compiling Kivy project to APK file.

## Step 1: Setting up Windows Subsystem for Linux (Windows Users ONLY)
### Install Windows Subsystem for Linux (WSL) [Link](https://learn.microsoft.com/en-us/windows/wsl/install-manual)
Ensure powershell is running as administrator and run the below commands
- [x] dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
- [x] dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
- [x] Now restart your computer for the effects to take place (installing the wsl)

### Download the Linux kernel update package
The Linux kernel update package installs the most recent version of the WSL 2 Linux kernel for running WSL inside the Windows operating system image.
- [x] [Download](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi) latest package
Open powershell and run the below command (set WSL 2 as the default version when installing a new Linux distribution)
- [x] wsl --set-default-version 2
- [x] Open the [Microsoft Store](https://aka.ms/wslstore) and select your favorite Linux distribution.

## Step 2: Getting started with your current working directory on your pc, and wsl
### Create your current working directory (cwd)
- [x] You want to create your cwd near the root folder of your pc. For example `c/Users/<yourname>/Documents/cwd`
Change `<yourname>` with your `pc name` or `username`, and cwd with your `project_folder_name`, where all your code will be hosted.

### Open your Linux Distribution from the Applications
1. If your Linux Distribution was Debian, go to Start/Windows Key, then run Debian, if it was Ubuntu, go to Start/Windows Key then run Ubuntu.
2. A terminal will open. Set your username and your password.
3. Now you will navigate from your wsl terminal to your cwd in your pc.</br>
   3.1 Copy the path of your current working directory. Should look something like this `c/Users/<yourname>/Documents/cwd`.</br>
   3.2 On your wsl terminal, write the following code **`cd/mnt/c/Users/<yourname>/Documents/cwd`**. Remember to adjust to fit your cwd, and username or pc name.
4. Good Progress!
## Step 3: Installing buildozer and its dependencies [Link](https://buildozer.readthedocs.io/en/latest/installation.html)

