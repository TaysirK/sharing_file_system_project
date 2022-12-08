import socket 

import threading

localIP     = "127.0.0.1"

localPort   = 20002

bufferSize  = 1024

DisconnectMsg="QUIT"

clients = set()

clients_lock = threading.Lock()

client_searching = set()



def findFile(file,connClient):

    print(file)

    for c in clients: 

        if c != connClient:

            try:

                print(' >>>>> sending\n')

                print(connClient)

                c.send(f'SEARCH :{file}'.encode("utf-8"))

            



            except:

                print('NONE')

    



def handle_client(conn,addr):

    if conn:

        clients.add(conn)



    connected = True

    while connected:

        msg=conn.recv(bufferSize).decode('utf-8')

        if msg  == DisconnectMsg:

            connected=False

        elif msg[:6] == 'FILE :':

            file=msg[6:]

            findFile(file,conn)

            client_searching.add(conn)

        elif msg[:6] == 'FOUND':

            print('this is the client that have th file : ')

            print(conn)

            print('this is the client searching : ')

            print(client_searching)

            conn.send(f'SERVER : 20010'.encode('utf-8'))

            for c in client_searching:

                c.send(f'CLIENT :20010'.encode('utf-8'))

   

        else:

            print(f"[{addr}]  : {msg}\n")

            break



    conn.close()



if __name__ == '__main__':

    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    server.bind((localIP,localPort))

    server.listen()

    print("[SERVER GP1] up and listening")



    while True:

        conn, addr = server.accept()

        thread = threading.Thread(target=handle_client,args=(conn,addr))

        thread.start()

        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")

    server.close()

        