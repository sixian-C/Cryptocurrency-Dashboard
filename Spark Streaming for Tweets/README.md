### How to install netcat command on your docker image
First, you need to get inside your docker image by typing:


```

docker exec -it -u root container_id bash

```

Then, you need to run 
```
sudo apt-get update
sudo apt-get install netcat
sudo apt-get install net-tools
```
Here, the docker image here I use is pyspark-notebook. When you run sudo apt-get, it will
ask you for password, one solution is to execute docker image with root permission. 


Find port and kill it 
```
netstat -ano|findstr 10708
tskill 14588
```