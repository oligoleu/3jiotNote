Nvidia Jetson Nano
===
<h3>user: od3j  IP: 192.168.50.157</h3>

|Package       |Version |                                               |
|:------------:|:------:|:---------------------------------------------:|
|nomachine     |6.12.3_5|		                                            |
|mosquitto     |1.4.15  |                                               |
|go            |1.15.4  |https://golang.org/dl/ (download ARMv8 version)|
|opencv        |		    |                                               |
|gocv          |        |                                               |
|cmake         |3.12.4  |https://cmake.org/install/                     |
|jtop          |		    |                                               |
|vsftp         |		    |                                               |
|darknet       |		    |                                               |
|jetson-fan-ctl|		    |https://github.com.Pyrestone/jetson-fan-ctl    |

-----
install cmake 
-----
>https://cmake.org/install/
#### step 1 : find the correct version and download sourcecode

```bash
$ cd /tmp
$ wget https://github.com/Kitware/CMake/archive/v3.12.4.tar.gz
$ sudo tar -C /tmp -xzf v3.12.4.tar.gz
```

#### step 2 : build cmake

```bash
$ cd CMake-3.12.4
$ sudo ./bootstrap
$ sudo make
$ sudo make install
```
#### step 3 : check cmake version

```bash
$ cmake --version 
```
