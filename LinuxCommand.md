## Backup Memory Card
### Using flash drive
記憶卡使用讀卡機讀取
#### step 1 
>Plug in the flash drive and mount drive with dir

```bash
$ fdisk -l    # find two disks that you want to mount(一個隨身碟的，一個記憶卡的)
$ mkdir p1    # create a dir 
$ sudo mount /dev/sdb1 p1
```

#### step 2
>compress the contents of memory card to p1
```bash
$ sudo dd if=/dev/sde | pv | gzip -9 > /p1/iso.gz # /dev/sde is memory card's disk
```
