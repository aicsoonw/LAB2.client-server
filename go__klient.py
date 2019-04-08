import socket

sock = socket.socket()
serverName = '127.0.0.1'
serverPort = 9090
sock.connect(('localhost', 9090))

arrayNum = input("Введите количество элементов массива")
aray=[]
for x in range(0, int(arrayNum)):
    arrayInput = input("Введите значение элемента ")
    aray.append(arrayInput)

print("Что вы хотите сделать с массивом?")
print("1 -- Максимальные значения")
print("2 -- Dывод элементов по введенным индексам и их произведение")
messageChoice = input("Ваш выбор :")
if messageChoice == "1":
    messageAdd = input("Введите количество максимальных чисел :")
elif messageChoice == "2":
    whileStop='n'
    messageAdd = ''
    while whileStop != 'y':
        newdata=input("Введите номер элемента")
        messageAdd = messageAdd + newdata + ';'
        whileStop=input("Все? [y/n]")

message = arrayNum

for x in range(0, int(arrayNum)):
    message = message + ";" + aray[x]
message = message + ";" + messageChoice
message = message + ";" + messageAdd

print(message)

sock.sendto(message.encode(), (serverName, serverPort))

data = sock.recv(1024)
data=str(data)

sock.close()

print(data)

data=data[2:-1]

print(data)

