# Datation 2
![GitHub](https://img.shields.io/github/license/alkanoidwastaken/datation-2?style=for-the-badge) ![GitHub all releases](https://img.shields.io/github/downloads/alkanoidwastaken/datation-2/total?style=for-the-badge) ![GitHub issues](https://img.shields.io/github/issues-raw/alkanoidwastaken/datation-2?style=for-the-badge)
###### A Python Calculator giving you calculations from your data, and making graphs.

Datation 2 takes a dataset, does calculations that give you the number of score, mean, median, mode, range, variance, low median and high median.
Then it outputs this, allows you to store it and gives you useful graphs.

This is a simple program that can be customized for different calculations and graphs.

## Executables
Prebuilt binaries are available:

[![Windows Installer][windows-badge]][windows-link] [![Mac Installer][mac-badge]][mac-link]

[windows-link]: https://github.com/Alkanoidwastaken/datation-2/releases/download/v2.0.0/windows-x86_64.exe
[windows-badge]: https://img.shields.io/badge/Windows%20-Download-3a71c1?logo=Windows&logoColor=3a71c1&labelColor=0c0d10&color=3a71c1&style=for-the-badge
[mac-link]: https://github.com/Alkanoidwastaken/datation-2/releases/download/v2.0.0/macos-arm
[mac-badge]: https://img.shields.io/badge/macOS%20%20-Download-3a71c1?logo=Apple&logoColor=3a71c1&labelColor=0c0d10&color=3a71c1&style=for-the-badge


## Manual Usage
If you want to develop this program, follow the instructions below.

### Prerequisites
- [Git](https://git-scm.com)
- [Python](https://www.python.org)
- Access to the command line

### 1: Clone the repository
```
git clone https://github.com/Alkanoidwastaken/datation-2.git
```
### 2: Install dependencies
##### Windows:
```
python setup.py
```
##### UNIX (Mac/Linux):
```
python3 setup.py
```
### 3: Run the program
##### Windows:
```
python main.py
```
##### UNIX (Mac/Linux):
```
python3 main.py
```
> This is the program. You can compile it using the steps below.

## Manual Compilation
### 1: Run setup.py
##### Windows:
```
python setup.py
```
##### UNIX (Mac/Linux):
```
python3 setup.py
```
### 2: Install cpython
#### Windows:
```
pip install cython
```
#### UNIX (Mac/Linux):
```
pip3 install cython
```
### 3: Convert to C File
```
cython main.py --embed
```
### 4: Compile
```
PYTHONLIBVER=python$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')$(python3-config --abiflags)
gcc -Os $(python3-config --includes) main.c -o main $(python3-config --ldflags) -l$PYTHONLIBVER
```
> The program will now compile into a executable named main
> Note: The executable will only be able to be used for your specific operating system and architecture
> For example: If you compiled it on a x86_64 Windows machine, it will only run on other x86_64 Windows machines.


```
By Alkanoid
```