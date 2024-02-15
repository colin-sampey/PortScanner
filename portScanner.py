import socket

#main contains a loop calling our helper method to try to test each port
# if the port is open, it'll add it to an array, which will be returned in either a file or print statements
def main():
    host = input("Enter the host: ")
    openPorts = []
    for num in range(80):
        if(isThePortOpen(host, num):
           openPorts.append(num))
    

# isThePort Open works by using the socket library to attempt connecting to the passed host and port number
# If it connects, it will return true, otherwise false
def isThePortOpen(host, port):
    testing = socket.socket()
    try:
        testing.connect((host, port))
    except:
        return False
    else:
        return True


main()
