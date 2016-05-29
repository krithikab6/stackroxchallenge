import docker,time
from docker import Client
client = docker.from_env(assert_hostname=False)
#Client(base_url='tcp://127.0.0.1:2375')
#print (client.version())
all=client.containers()

if all[0]['Image'] == 'swarm' and all[0]['State'] =='running':
	print ('Swarm manager is running')
	c=client.create_container(image='swarm',command='-v')
	id=c.get('Id')
	print (id)
	client.start(container=c.get('Id'))
	time.sleep(0.10)
	t=client.logs(c.get('Id'))
	text=t.decode()
	arr=text.split(' ')
	version=arr[len(arr)-2]
	numarr=version.split('.')
	num=float(numarr[0]+'.'+numarr[1])
	if num<1.7:
	      raise Exception('Version', 'Invalid')
	else:
	 print (client.info())  
else:
	 raise Exception('Swarm manager', 'not running')	  
#bc606f60631903ab257409ac009aaa19
#645e5a148fec7f3c945f90f192c45c25fa9d14d
#b120e622da1990e8e97588c4a
# docker run -d -p 3376:3376 -t -v /var/lib/boot2docker:/certs:ro swarm manage -H 0.0.0.0:3376 --tlsverify --tlscacert=/certs/ca.pem --tlscert=/certs/server.pem --tlskey=/certs/server-key.pem token://bc606f60631903ab257409ac009aaa19
#docker run -d swarm join --addr=$(docker-machine ip agent3):2376 token://bc606f60631903ab257409ac009aaa19