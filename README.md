This program is based on sockets

it has server and client in the folder , make sure that this program is used under a LAN Network

The server and clients in the file need a same Gateway which is the router ip address (eg. 10.57.0.1)

Main motive of this program is to control the Games unsing mobile application the moblie application is in Remote_10.py program run that program in a mobile connected to wifi

use : >>> Pydroid 3 app to run the Remote_10 program

Steps to run the program :

git clone https://github.com/kalivarun/Desktop_controller.git

cd WIFI_Dev_Remote

ls

pip install -r Requirements.txt

nano client.py

search for client.connect(('127.0.0.1', 5000))

Change 127.0.0.1 to

python3 multi_server.py

Open new tab

cd WIFI_Dev_Remote

pyinstaller --onedir client.py

ls

cd dist

ls | grep client.exe

send the client.exe to target pc

run client.exe in target pc

go back to terminal

ls

nano Remote_10.py

Search for host = socket.gethostbyname(socket.gethostname()) #host = '10.76.15.246' Change it as #host = socket.gethostbyname(socket.gethostname()) host = '<multi_server.py --ipaddress>' #change the ip address with the server ip address

Copy whole code of Remote_10.py and now install Pydroid 3 in your mobile

Make sure the mobile is connected to same router as the multi_server.py and client.exe

now past the whole code of Remote_10.py in new folder in Pydroid 3 in mobile

now open a Online car game in Client.exe pc > suggested to open NFS 2018 in pc

now you will find a GUI in mobile after running the Remote_10.py in mobile (make sure the multi_server.py and Client.exe are running in different systems)

press the buttons on the mobile to control the Game running on the Client.exe system.






