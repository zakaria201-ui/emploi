import paramiko

#Créer une instance de l'objet SSHClient
client = paramiko.SSHClient()

# Ajouter l'host key policy (ignorer pour l'exemple)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Se connecter à l'hote distant
#client.connect('hostname', username='username', password='password')
client.connect('192.168.100.1', username='root', password='passer')

# Executer une commande à distance
#stdin, stdout, stderr = client.exec_command('rm -rf test*')
stdin, stdout, stderr = client.exec_command('mkdir isi')

# Afficher la sortie de la commande
for line in stdout:
    print(line.strip())
    

#Fermer la connexion ssh
client.close()