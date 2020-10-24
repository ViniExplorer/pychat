import client, server, socket

# Starting up the app
print("Chatroom App, fork from Zhang Zeyu's chatapp.\nCheck out https://github.com/zeyu2001/pychat\n")

print("Your IP is", socket.gethostbyname(socket.gethostname()))

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
