import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print('connected:' + str(addr))


while True:
    data = conn.recv(1024)
    if not data:
        break
    data=str(data)
    data=data[2:-1]
    data = data.split(';')
    aray = []
    for x in range(0, int(data[0])):
        aray.append(int(data[1+x]))
    print(data)
    print(aray)

    if data[1+int(data[0])] == '1':
        dataSort = sorted(aray, key = int, reverse=True)
        dataIndex = int(data[2+int(data[0])])
        dataSort = dataSort[:dataIndex]
        print(dataSort)
        message=''
        for x in range(0, len(dataSort)):
            message = message + str(dataSort[x]) + ';'
        print(message)
        conn.send(message.encode())
    elif data[1+int(data[0])] == '2':
        data = data[2+int(data[0]):-1]
        print(data)
        message = ''
        for x in range(0, len(data)):
            message = message + str(aray[int(data[x])]) + ';'
        print(message)
        conn.send(message.encode())
conn.close()