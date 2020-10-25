import client, server, socket, time

# Starting up the app
print("Chatroom App, fork from Zhang Zeyu's chatapp.\nCheck out https://github.com/zeyu2001/pychat\n")

print("Your IP is", socket.gethostbyname(socket.gethostname()))

def LookForServers():
    # Setting up the socket to listen to on UDP protocol
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 127.16.1.255 is the IP for all local network devices
    s.bind(('127.16.1.255', 1060))

    print("Checking if any servers are online...")
    for i in range(5):
        msg, addr = s.recvfrom(1060)
        if msg == "ONLINE":
            print(f"Received message from {addr}!")
            choice = input("Would you like to connect to this server? (y/n)")
            if (choice == "y"):
                client.start(addr, 1060)

# This is to see if the user wants to check if someone has
# a server that's already on
print("Check for servers online? (y/n)", end="")
c = input()

if c == "y":
    LookForServers()


# An int which will be the user's choice
# on what they will do
choice = 0

while True:
    try:
        choice = int(input("Choose something to do: \n1 - Run a client\n2 - Run a server\n3 - Host and be a client\n"))
        break
    except:
        print("Invalid answer. Try again.")

if choice == 1:
    while True:
        # Taking in parameters to connect to the server
        try:
            ip = input("IP: ")
            port = int(input("Port: "))
            break
        except:
            print("Invalid answer. Try again.")
    client.start(ip, port)
elif choice == 2:
    server.start("localhost", 1060)
elif choice == 3:
    server.start("localhost", 1060)
    client.start("localhost", 1060)
