Docker
-----
#### step 1 : Update the apt package index
```bash
$ sudo apt update
```
#### step 2 : Install packages to allow apt to use a repository over HTTPS
```bash
$ sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release
```
#### step 3 : Add Docker’s official GPG key
```bash
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```
#### step 4 : Set up the stable repository
#### To add the nightly or test repository, add the word nightly or test (or both) after the word stable in the commands below
> Note: The lsb_release -cs sub-command below returns the name of your Ubuntu distribution, such as xenial. 
> Sometimes, in a distribution like Linux Mint, you might need to change $(lsb_release -cs) to your parent Ubuntu distribution. 
> For example, if you are using Linux Mint Tessa, you could use bionic. 
> Docker does not offer any guarantees on untested and unsupported Ubuntu distributions.
```bash
$ sudo apt update
```
#### step 5 : Install the latest version of Docker Engine and container
```bash
$ sudo apt-get install docker-ce docker-ce-cli containerd.io
```
#### step 6 : Verify that Docker Engine is installed correctly by running the hello-world image
```bash
$ sudo docker run hello-world
```
#### step 7 : Check docker version
```bash
$ docker version
```
