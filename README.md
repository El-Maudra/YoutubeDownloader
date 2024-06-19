# YoutubeDownloader

## Install Windows Subsystem for Linux (WSL) [Link](https://learn.microsoft.com/en-us/windows/wsl/install-manual)
Ensure powershell is running as administrator and run the below commands
- [x] dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
- [x] dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
- [x] Now restart your computer for the effects to take place (installing the wsl)

## Download the Linux kernel update package
The Linux kernel update package installs the most recent version of the WSL 2 Linux kernel for running WSL inside the Windows operating system image.
- [x] [Download](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi) latest package
Open powershell and run the below command (set WSL 2 as the default version when installing a new Linux distribution)
- [x] wsl --set-default-version 2
- [x] Open the [Microsoft Store](https://aka.ms/wslstore) and select your favorite Linux distribution.


