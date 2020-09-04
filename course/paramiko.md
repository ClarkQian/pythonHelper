# ssh
## send command
1. import paramiko.SSHClient()
2. ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
  > make sure that the connection will be create wheater there is `unknown host`
3. ssh.connect(hostname='localhost', port=22, username='root', password="1234")

4. get result 
  >stdin, stdout, stderr  = ssh.exec_command("ls")  
  >stdin is cmmd, stdout/stderr is the output
5. get result and print
  >result = stdout.read()  
  >print(result.decode())
6. ssh.close()
## ftp function
1. import paramiko
2. create the transport
  >transport = paramiko.Transport(('',22))  
  >transport.connect(username="root", password="")
3. create sftp instance
  >sftp = paramiko.SFTPClient.from_transport(transport)
4. ftp work
  >sftp.put('./__init__.py', '/root/test/test.py')  
  >sftp.get('/root/test/test.cpp','./test.cpp')
  
  ```
  unknown host means ~/.ssh/.knownhost has no record
  you can use ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
  ```
 
 ## using RSA(非对称密钥) key to connect ssh instead of password
 ### theory
 compare with each other  
 10.0.0.31           no password ssh         10.0.0.41（save 10.0.0.31's public rsa）
 private key         ->>                  public key  
 10.0.0.31 send `public key` to 10.0.0.41
 > 可以使用指令 ssh-copy-id "-p22 root@10.0.0.31" 添加key到目标机器
 ```
    
    ☢authorized_keys必须保证是644不能是别的
 ```
 ## using rsa to enter
 1. save the id_rsa(created private one, be used to connect)
 2. load the rsa by
 >private_key = paramiko.RSAKey.from_private_key_file('/home/auto/.ssh/id_rsa')   
 >ssh.connect(username="" pkey=private_key)
