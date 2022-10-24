# Datation 2
![GitHub](https://img.shields.io/github/license/alkanoidwastaken/datation-2?style=for-the-badge) ![GitHub all releases](https://img.shields.io/github/downloads/alkanoidwastaken/datation-2/total?style=for-the-badge) ![GitHub issues](https://img.shields.io/github/issues-raw/alkanoidwastaken/datation-2?style=for-the-badge)
###### A Python Calculator giving you calculations from your data, and making graphs.

Datation 2 takes a dataset, does calculations that give you the number of score, mean, median, mode, range, variance, low median and high median.
Then it outputs this, allows you to store it and gives you useful graphs.

This is a simple program that can be customized for different calculations and graphs.

## Executables
Prebuilt binaries are available:

[![Universal Installer][universal-badge]][universal-link]

[universal-link]: https://github.com/Alkanoidwastaken/datation-2/releases/download/v2.0.1/main
[universal-badge]: https://img.shields.io/badge/Universal%20-Download-3a71c1?logo=Python&logoColor=3a71c1&labelColor=0c0d10&color=3a71c1&style=for-the-badge


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
### 1: Install cpython
```
sudo -H pip3 install cython
```
### 2: Generate a C file
```
cython main.py --embed
```
### 3: Compile
```
PYTHONLIBVER=python$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')$(python3-config --abiflags)
gcc -Os $(python3-config --includes) main.c -o main $(python3-config --ldflags) -l$PYTHONLIBVER
```
> The program will now compile into a file named main (executable)


```
By Alkanoid
```
