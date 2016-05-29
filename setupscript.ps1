param (
    [string]$dockertool
	)
docker-machine create -d virtualbox master11
& $dockertool env master11
& $dockertool env master11 | Invoke-Expression
docker-machine create -d virtualbox sslave1
& $dockertool env sslave1
& $dockertool env sslave1 | Invoke-Expression
& $dockertool env master11 | Invoke-Expression
docker pull swarm
$clusterid = docker run --rm swarm create
docker run -d -p 3376:3376 -t -v /var/lib/boot2docker:/certs:ro swarm manage -H 0.0.0.0:3376 --tlsverify --tlscacert=/certs/ca.pem --tlscert=/certs/server.pem --tlskey=/certs/server-key.pem token:$clusterid
& $dockertool env sslave1 | Invoke-Expression
docker run -d swarm join --addr=$(docker-machine ip sslave):2376 token://$clusterid
& $dockertool env master11 | Invoke-Expression