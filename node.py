import socket

from PIL import Image

import threading

import os

import tqdm

from threading  import *

import time





fileSearched = ''

testclient=False

testServer=False

serverAddressPort   = ("127.0.0.1", 20002) 

def clientClient():        

        

        print('here2')



        #client.close()



        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        time.sleep(3)

        conn.connect(('127.0.0.1',6000))

        file_name=conn.recv(1024).decode()

        print(file_name)

        file_size=conn.recv(1024).decode()

        print(file_size)



        file = open(file_name,"wb")

        file_bytes= b""

        done=False

        try:

                progress = tqdm.tqdm(unit="B",unit_scale=True,unit_divisor=1000,

                total=int(file_size))



                while not done:

                        data = conn.recv(1024)

                        if file_bytes[-5:] == b"<END>":

                                done = True

                        else : 

                                file_bytes += data

                                progress.update(1024)



                        file.write(file_bytes)

                        file.close()

        except:

                pass

        conn.close()

def clientServer():                

        

                        print('hre2')

                        #client.close()

                        

                        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                        cs.bind(('127.0.0.1',6000))

                        cs.listen()

                        conn , addr = cs.accept()

                        

                        with conn:

                                file  = open('lilith.txt',"rb")

                                file_size=os.path.getsize('lilith.txt')

                                conn.send("lily.txt".encode('utf-8'))

                                conn.send(str(file_size).encode('utf-8'))



                                data =file.read()

                                conn.sendall(data)

                                conn.send(b"<END>")



                                file.close()

                                

         





def clientSearch():

        global connected 

        connected = True

        while connected:

                File=input("What file you're looking for :\n> ") 

                client.send(f'FILE :{File}'.encode("utf-8"))



def clientFind():

        global connected

        while connected:

                Msg=client.recv(1024).decode('utf-8')

                

                if Msg[:6]== 'SEARCH' :

                        print(Msg[8:])

                        with open('ressource.txt') as file:

                                for line in file: 

                                        if line.rstrip() == Msg[8:]:

                                                print('FOUND')

                                                client.send('FOUND'.encode('utf-8'))

                                                break

                                        else:

                                                print('NOT FOUND')

                                                client.send('NOT FOUND'.encode('utf-8'))

                elif Msg[:6] == 'SERVER' : 

                        connected = False

                        print('here1')

                        client.close()

                        clientServer()

                        print('here3')

   

                elif Msg[:6] == 'CLIENT':

                        

                        connected = False

                        print('here1')

                        client.close()

                        clientClient()

                        print('here3')                               

                else:

                        print('NONE')



       

class bcolors:

    HEADER = '\033[95m'

    OKBLUE = '\033[94m'

    OKCYAN = '\033[96m'

    OKGREEN = '\033[92m'

    WARNING = '\033[93m'

    FAIL = '\033[91m'

    ENDC = '\033[0m'

    BOLD = '\033[1m'

    UNDERLINE = '\033[4m'

        







if __name__ == '__main__':

        print('\n\n')

        print(f"{bcolors.OKBLUE}        ***************************************************{bcolors.BOLD}")

        print(f"{bcolors.OKBLUE}        ***************    WELCOME MATE!    ***************{bcolors.BOLD}")

        print(f"{bcolors.OKBLUE}        ***************************************************{bcolors.ENDC}")

        print(f"{bcolors.OKBLUE}        ***************************************************{bcolors.ENDC}")

        print('\n\n')

        

        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        client.connect(serverAddressPort)

        print("Connected to the server")

        thread1 = threading.Thread(target=clientSearch)

        thread2 = threading.Thread(target=clientFind)

        thread1.start()

        thread2.start()



        thread1.join()

        thread2.join()