|Package       |Version |                                               |
|:------------:|:------:|:---------------------------------------------:|
|Docker        |20.10.6 |https://docs.docker.com/engine/install/ubuntu/ |
|Docker Compose|1.29.2  |https://docs.docker.com/compose/install/       |
|Redis         |6.2.4   |https://codewithhugo.com/install-just-redis-cli-on-ubuntu-debian-jessie/|
|mongoDB       |3.6.8	  |https://www.mongodb.com/try/download/mongocli|

Docker
-----
#### step 1 : Update the apt package index
```bash
$ sudo apt update
```
#### step 2 : Install packages to allow apt to use a repository over HTTPS
```bash
$ sudo apt install apt-transport-https ca-certificates curl gnupg lsb-release
```
#### step 3 : Add Docker’s official GPG key
```bash
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```
#### step 4 : Set up the stable repository

> Note: The lsb_release -cs sub-command below returns the name of your Ubuntu distribution, such as xenial. 
> Sometimes, in a distribution like Linux Mint, you might need to change $(lsb_release -cs) to your parent Ubuntu distribution. 
> For example, if you are using Linux Mint Tessa, you could use bionic. 
> Docker does not offer any guarantees on untested and unsupported Ubuntu distributions.

```bash
$ echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
#### step 5 : Update the apt package index and install the latest version of Docker Engine and container
```bash
$ sudo apt update
$ sudo apt install docker-ce docker-ce-cli containerd.io
```
#### step 6 : Verify that Docker Engine is installed correctly by running the hello-world image
```bash
$ sudo docker run hello-world
```
#### step 7 : Check docker version
```bash
$ docker version
```
Docker Compose
-----
#### step 1 : Download the current stable release of Docker Compose
```bash
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
#### step 2 : Apply executable permissions to the binary
```bash
$ sudo chmod +x /usr/local/bin/docker-compose
```
#### step 3 : Check docker compose version
```bash
$ docker-compose --version
```
Redis-clients
-----
#### step 1 : Download the current stable release of Redis
```bash
$ cd /tmp
$ wget http://download.redis.io/redis-stable.tar.gz
```
#### step 2 : Unpack the file
```bash
$ tar xvzf redis-stable.tar.gz
```
#### step 3 : install package and make
```bash
$ cd redis-stable
$ sudo apt install libjemalloc1 libjemalloc-dev gcc make
$ make
```
#### step 3 : Copy file and apply executable permissions to the binary
```bash
$ sudo cp src/redis-cli /usr/local/bin/
$ sudo chmod 755 /usr/local/bin/redis-cli
```
#### step 4 : Change folder name and copy folder to /etc
```bash
$ cd ..
$ mv redis-stable/ redis
$ sudo cp -r redis /etc/
```
#### step 5 : Change the bind host and port on redis.conf
```bash
$ sudo nano /etc/redis/redis.conf
```
#### step 6 : Check redis-cli version
```bash
$ redis-cli --version
```
#### step 7 : Using redis-cli
```bash
$ redis-cli -h host -p port
```
Mongodb-clients
-----
#### step 1 : Download mongodb-clients
```bash
$ sudo apt install mongodb-clients
```
#### step 2 : Check redis-cli version
```bash
$ mongo --version
```
#### step 3 : Using mongo
```bash
$ mongo host
```
