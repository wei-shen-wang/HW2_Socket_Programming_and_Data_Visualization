import socket
import json
import matplotlib.pyplot as plt
HOST = '0.0.0.0' # Standard loopback interface address
PORT = 1200 # Port to listen on (use ports > 1023)
totaldata = ""
NUMBER_OF_DATA = 100
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        data = ""
        while data[-4:-1]!="100":#read in 100 data
            data = conn.recv(1024).decode('utf8')
            left = -1
            right = -1
            for i in range(len(data)):
                #parsing data because sometime the server receive two sets of data in one message
                if(data[i]=="{"):
                    left = i
                elif(data[i]=="}"):
                    right = i
                    totaldata += ","+data[left:right+1]
            print('Received from socket server : ', data)
jsloads = json.loads("["+totaldata[1:]+"]")#load a list of dictinary

month = [0]*NUMBER_OF_DATA
x = [0]*NUMBER_OF_DATA
y = [0]*NUMBER_OF_DATA
z = [0]*NUMBER_OF_DATA
for i in range(NUMBER_OF_DATA):
    month[i] = i+1
    x[i] = jsloads[i]["x"]
    y[i] = jsloads[i]["y"]
    z[i] = jsloads[i]["z"]
plt.figure(figsize=(15,10),dpi=100,linewidth = 2)

plt.plot(month, x, 's-',color = 'r', label="magento_x")
plt.plot(month, y, 'o-', color = 'g', label="magento_y")
plt.plot(month, z, 'o-', color = 'b', label="magento_z")


plt.title("magneto xyz line chart", x=0.5, y=1.03, fontsize = 40)

plt.xticks(fontsize=20)

plt.yticks(fontsize=20)

plt.xlabel("no of data", fontsize=30, labelpad = 15)

plt.ylabel("magneto data", fontsize=30, labelpad = 20)

plt.legend(loc = "best", fontsize=20)

plt.show()
