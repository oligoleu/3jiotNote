## Darknet
>https://github.com/AlexeyAB/darknet
#### step 1 :
```bash
$ mkdir projects
$ cd projects/
$ git clone https://github.com/AlexeyAB/darknet.git
```
#### step 2 : change Makefile setting
```bash
$ cd darknet/
$ nano Makefile
```
As below
```vim
GPU=1 
CUDNN=1
CUDNN_HALF=0
OPENCV=1
AVX=0
OPENMP=1
LIBSO=1
ZED_CAMERA=0
ZED_CAMERA_v2_8=0
```
And build darknet
```bash
$ ./build.sh
```
If you have problem like this "error: unrecognized command line option ‘-mavx’ "
```bash
$ nano CMakeLists.txt
```
Annotation two lines 
```vim
# set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -ffp-contract=fast -mavx -mavx2 -msse3 -msse4.1 -msse4.2 -msse4a")
# set(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} -ffp-contract=fast -mavx -mavx2 -msse3 -msse4.1 -msse4.2 -msse4a")
```
#### step 3 : check
' ldd ' prints the shared objects (shared libraries) required by each program or shared object 
specified on the command line.
```bash
$ ldd ./libdarknet.so 
$ ldd ./darknet
```
