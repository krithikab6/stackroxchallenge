Vagrant.configure("2") do |config|
  config.vm.provision "docker",
  images: ["swarm"]
  config.vm.define "master" do |master|
    master.vm.box = "ubuntu/trusty64"
  end
 config.vm.define "slave" do |slave|
    slave.vm.box = "ubuntu/trusty64"
  end
end
