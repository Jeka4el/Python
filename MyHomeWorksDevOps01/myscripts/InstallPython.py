import distro
import subprocess

def install_python():
    #distro_info = distro.linux_distribution(full_distribution_name=False)
    #distro_version = distro_info[0]
    distro_info = distro.id()
    distro_version = distro_info
    commands = []
    if distro_version in ('debian', 'ubuntu'):
        commands =  [
            "sudo apt-get update",
            "sudo apt-get install -y build-essential zlib1g-dev libffi-dev libssl-dev",
            "wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tar.xz",
            "tar -xvf Python-3.7.2.tar.xz",
            "cd Python-3.7.2 && ./configure && make -j 2 && sudo make altinstall",
           # "pwd ; ",
           # "./configure",
           # "make -j 2 ; "
           # "sudo make altinstall ; "
           # "cd .. ; ",
           "rm -rf Python-2.7.2 Python-3.7.2.tar.xz"
        ]
        for command in commands:
            print("Executing:", command)
            subprocess.run(command, shell=True)
    elif distro_version in ('rhel'):
        commands = [
           "sudo yum update",
           "sudo yum install wget",
           "sudo yum groupinstall -y 'Development Tools'",
           "sudo yum install -y zlib-devel libffi-devel openssl-devel",
           "wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tar.xz",
           "tar -xvf Python-3.7.2.tar.xz",
           "cd ./Python-3.7.2 && ./configure && make && sudo make altinstall",
           "rm -rf Python-2.7.2 Python-3.7.2.tar.xz"
        ]
        for command in commands:
            print("Executing:", command)
            subprocess.run(command, shell=True)



    else:
        print(f"Дистрибутив {distro_version} не поддерживается.")
    return


        #print("Distro Version:", distro_version)


install_python()
