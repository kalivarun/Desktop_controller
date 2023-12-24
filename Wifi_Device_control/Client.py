import socket
import threading
import pyautogui as pi 
import ctypes
import webbrowser
import os
import smtplib
import ssl
from email.message import EmailMessage


ip_addr = socket.gethostbyname(socket.gethostname())






def to_mail_ip_address():
        
    
        sender = "k.s.varunchandra@gmail.com"
        sender_psd = "vxfl vsam lhwc jtnn"
        res = "k.s.varunchandra@gmail.com" #modify here change with your mail id 
        subject = 'DEVICE DETAILS '
        body1 = f'ip address of conneting device :{ip_addr}'

        em = EmailMessage()
        em.set_content(body1)
        em['Subject'] = subject
        em['From'] = sender
        em['To'] = res
        try:
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                      smtp.login(sender, sender_psd)
                      smtp.send_message(em)
                print("Email sent successfully!")
        except Exception as e:
                print("An error occurred:", e)
                f=0
        print(ip_addr)

if __name__ == "__main__":
    to_mail_ip_address()


print("""

1111             1111  11111111111   111         111111111111   111111111111   1111111    1111111    1111111111
 1111           1111   11111111111   111         111111111111   111111111111   1111111    1111111    1111111111
  1111         1111    1111          111         111            111      111   1111  111111  1111    111
   1111       1111     11111111111   111         111            111      111   1111    11    1111    1111111111
    1111  11 1111      11111111111   111         111            111      111   1111          1111    1111111111
     11111111111       1111          1111111111  111111111111   111111111111   1111          1111    111
      1111 1111        11111111111   1111111111  111111111111   111111111111   1111          1111    1111111111



000     000  000 0000        vvv     vvv  aaaa     rrr rrrr  uuu   uuu  nnn nnnnn
0000   0000  0000             vvv   vvv  aa  aa    rrrr      uuu   uuu  nnnn  nnn
000 000 000  000               vvv vvv  aaaaaaaa   rrr       uuu   uuu  nnn    nn
000     000  000                vvvv    aa    aa   rrr       uuuu uuuu  nnn    nn
000     000  000       O         vv     aaa   aaa  rrr         uuuuu    nnn    nn  ~Chandra



                                       > This client was specially designed for NFS-2018 

                                       > Make sure multi_server.py is online 
                                       
                                       > This tool is for controlling 
                                         Desktops connected to your LAN (router)     """)

def lock_screen():
    system_platform = os.name

    if system_platform == 'nt':  # Windows
        ctypes.windll.user32.LockWorkStation()
        os.system("rundll32.exe user32.dll,LockWorkStation")
    elif system_platform == 'posix':  # Linux or macOS
        os.system("gnome-screensaver-command -l")
    else:
        print("Unsupported operating system")







def open_google():
    webbrowser.open("")





def receive_messages():
    while True:
        try:
            data = client.recv(1024)
            if not data:
                break
            decoded_data = data.decode('utf-8')
            print(decoded_data)
            if decoded_data == 'Button Pressed ACC':
                pi.keyDown('up')

            elif decoded_data == 'Button Released ACC':
                pi.keyUp('up')

            elif decoded_data == 'Button Pressed BREAK':
                pi.keyDown('down')
            elif decoded_data == 'Button Released BREAK':
                pi.keyUp('down')


            elif decoded_data == 'Button Pressed HAND BREAK':
                pi.keyDown('space')

            elif decoded_data == 'Button Released HAND BREAK':
                pi.keyUp('space')
                
            elif decoded_data == 'Button Pressed RIGHT':
                pi.keyDown('right')
            elif decoded_data == 'Button Released RIGHT':
                pi.keyUp('right')

            elif decoded_data == 'Button Pressed LEFT':
                pi.keyDown('left')
            elif decoded_data == 'Button Released LEFT':
                pi.keyUp('left')

            elif decoded_data == 'Button Pressed BOOST':
                pi.keyDown('shiftleft')
            elif decoded_data == 'Button Released BOOST':
                pi.keyUp('shiftleft')
                
            elif decoded_data == 'Button Pressed CHANGE CAR':
                pi.keyDown('e')
            elif decoded_data == 'Button Released CHANGE CAR':
                pi.keyUp('e')
                

            elif decoded_data == 'Button Pressed ENTER':
                pi.keyDown('enter')
            elif decoded_data == 'Button Released ENTER':
                pi.keyUp('enter')

            elif decoded_data == 'Button Pressed EASY DRIVE':
                pi.keyDown('6')
                #if __name__ == "__main__":
                 #    open_google()

            elif decoded_data == 'Button Released EASY DRIVE':
                pi.keyUp('6')
                #print('dd')
            # ... (other key press and release blocks)

            elif decoded_data == 'Button Pressed ESC':
                pi.keyDown('esc')
                #lock_screen
                #ctypes.windll.user32.LockWorkStation()
            elif decoded_data == 'Button Released ESC':
                pi.keyUp('esc')
                #print('ss')

# ... (other key press and release blocks)


                                
        except:
            break

# Client setup
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5000))

# Start a thread to receive messages from the server
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Main client loop
while True:
    # Get user input and send it to the server
    message = input()
    client.send(message.encode('utf-8'))

