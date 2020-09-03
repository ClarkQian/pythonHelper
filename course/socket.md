# socket

## client

1. Import socket
2. Connet to the server by connection((only one param))  

> param in the format of (`public ip`, `port`)

3. send message by the function send(byte)

   > you must use b'string' to make sure that the message is byte in python3 or "中文".encode("utf-8")

- or you can get data by using recv(the size of packet)

4. close the connection by close()

   

## server

1. import socket

2. Bind((`socket`))

   > ⚠️ in aliyun's server you must use you private ip to listen instead of public one

3. listen to the port

4. accept the requst instance by conn, address = accept()

   > ⚠️ you can't work like client by only get or send a request, you must divid different instance for different session by using accept and using the instance to realize some useful functions.

5. get or send the message the same as above

   > if message is Chinese you have to transfer the bytes to String, you have to decode() to Chinese

## addition

1. Big data you can use sendall(data) to send all the file, which can bee seen as while using send.

2. if server using wihile to make sure that the connection is maintained, there will be a infinite loop, which caused by recv() always get `""`, to avoid this situation, you must add following code

   ```python
   data = conn.recv(1024)
   if not data:
     break
   ```

3. if server send `""`, actually there is no send back, and the client will wait the respond forever, which will contribute to the infinite loop

## demo

```python
'''
	ftp demo
'''
# client.py
import socket

'''
this is client
'''

client = socket.socket()
client.connect(('localhost',58897))
while True:
    file = input("please enter:").strip()
    client.send(file.encode())
    if not file:
        print("empty")

        continue
    size = client.recv(1024)
    client.send('hh'.encode())
    fileContent = client.recv(1024)
    # print(fileContent.decode())
    with open('./recv/%s'%file, 'wb') as f:
        f.write(fileContent)
    print('finishing writing')
    client.close()
    break;
    
    
#server.py
import socket
import time

'''
this is server
'''

server = socket.socket()
server.bind(('localhost',58897))
server.listen()
while True:
    conn, add = server.accept()
    while True:
        try:
            print('wating for file')
            file_name = conn.recv(1024).decode()
            if file_name == 'q':
                break;
            if not file_name:
                conn.close()
                break;
            print("The file is %s"%file_name)

            f = open('./file/%s'%file_name,'r')
            file = f.read()
            file_size = conn.send(str(len(file)).encode())
            c = conn.recv(100)
            conn.sendall(file.encode())
        except Exception as e:
            print(e)
            conn.close()
            break;

```



