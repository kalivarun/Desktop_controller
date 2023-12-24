import socket
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

host = socket.gethostbyname(socket.gethostname())
#host = '10.76.15.246'
port = 5000

# Create a socket object outside the loop
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

class Main(App):
    def build(self):
        layout = BoxLayout(orientation='horizontal', spacing=17, padding=16)
        
        # Left column
        left_column = BoxLayout(orientation='vertical', spacing=10)
        btn1 = Button(text="BOOST", color="white", on_press=self.btn1_press, on_release=self.btn1_release)
        btn2 = Button(text="CHANGE CAR", color="white", on_press=self.btn2_press, on_release=self.btn2_release)
        btn_e = Button(text="ENTER", color="white", on_press=self.btn_e_press, on_release=self.btn_e_release)
        btn7 = Button(text="EASY DRIVE", color="white", on_press=self.btn7_press, on_release=self.btn7_release)
        btn8 = Button(text="ESC", color="white", on_press=self.btn8_press, on_release=self.btn8_release)
        
        left_column.add_widget(btn1)
        left_column.add_widget(btn2)
        left_column.add_widget(btn_e)
        left_column.add_widget(btn7)
        left_column.add_widget(btn8)
        

        # Right column
        right_column = BoxLayout(orientation='vertical', spacing=10)
        btn3 = Button(text="GO", color="white", on_press=self.btn3_press, on_release=self.btn3_release)
        btn4 = Button(text="BREAK", color="white", on_press=self.btn4_press, on_release=self.btn4_release)
        btn_h = Button(text="HAND BREAK", color="white", on_press=self.btn_h_press, on_release=self.btn_h_release)
        btn5 = Button(text="RIGHT", color="white", on_press=self.btn5_press, on_release=self.btn5_release)
        btn6 = Button(text="LEFT", color="white", on_press=self.btn6_press, on_release=self.btn6_release)

        right_column.add_widget(btn3)
        right_column.add_widget(btn4)
        right_column.add_widget(btn_h)
        right_column.add_widget(btn5)
        right_column.add_widget(btn6)
        

        # Add columns to the main layout
        layout.add_widget(left_column)
        layout.add_widget(right_column)

        return layout

    def send_message(self, message):
        client.send(message.encode('utf-8'))

    def btn1_press(self, btn1):
        print('button 1 pressed')
        self.send_message('Button Pressed BOOST')

    def btn1_release(self, btn1):
        print('button 1 released')
        self.send_message('Button Released BOOST')

    def btn2_press(self, btn2):
        print('button 2 pressed')
        self.send_message('Button Pressed CHANGE CAR')

    def btn2_release(self, btn2):
        print('button 2 released')
        self.send_message('Button Released CHANGE CAR')    

    def btn3_press(self, btn3):
        print('button 3 pressed')
        self.send_message('Button Pressed ACC')

    def btn3_release(self, btn3):
        print('button 3 released')
        self.send_message('Button Released ACC')

    def btn4_press(self, btn4):
        print('button 4 pressed')
        self.send_message('Button Pressed BREAK')

    def btn4_release(self, btn4):
        print('button 4 released')
        self.send_message('Button Released BREAK')
        
    def btn5_press(self, btn5):
        print('button 5 pressed')
        self.send_message('Button Pressed RIGHT')

    def btn5_release(self, btn5):
        print('button 5 released')
        self.send_message('Button Released RIGHT') 
        
    def btn6_press(self, btn6):
        print('button 6 pressed')
        self.send_message('Button Pressed LEFT')

    def btn6_release(self, btn6):
        print('button 6 released')
        self.send_message('Button Released LEFT')
        
    def btn7_press(self, btn7):
        print('button 7 pressed')
        self.send_message('Button Pressed EASY DRIVE')

    def btn7_release(self, btn7):
        print('button 7 released')
        self.send_message('Button Released EASY DRIVE')
        
    def btn8_press(self, btn8):
        print('button 8 pressed')
        self.send_message('Button Pressed ESC')

    def btn8_release(self, btn8):
        print('button 8 released')
        self.send_message('Button Released ESC')         

    def btn_e_press(self, btn_e):
        print('button e pressed')
        self.send_message('Button Pressed ENTER')

    def btn_e_release(self, btn_e):
        print('button e released')
        self.send_message('Button Released ENTER')


    def btn_h_press(self, btn_h):
        print('button h pressed')
        self.send_message('Button Pressed HAND BREAK')

    def btn_h_release(self, btn_h):
        print('button h released')
        self.send_message('Button Released HAND BREAK')


if __name__ == "__main__":
    Main().run()
        
