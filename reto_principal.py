import os, pygame , eyed3 , random , time, serial
import mutagen
import tkinter as tk
from PyQt5 import QtGui, QtCore

from reto_fin import *

#libreriar para la musica
from pygame.locals import *
from pygame.compat import geterror
from pygame import mixer
pygame.mixer.init()
import RPi.GPIO as GPIO
import serial
from PyQt5 import QtGui, QtCore
#libreriar para la oled
from PIL import Image, ImageDraw, ImageFont
from board import SCL, SDA
import busio
import adafruit_ssd1306
x2=""
x3=""
x4=0
x5=0
a=""
b=""
c=""
d=""
e=""
lin1=""
x=0
m=0
t=0
s=0
z=0
i=0
var=0


i2c = busio.I2C(SCL, SDA)
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
image = Image.new('1',(128,64))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 50)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 9)
font3 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)

ser = serial.Serial(
port= "/dev/ttyACM0",
baudrate = 19200,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,timeout=1)


class Cancion:
    def __init__(self,num,archivo):
        self.num = num

        self.archivo=  archivo

    def getNum(self):
        return self.num
    def getArchivo(self):
        return self.archivo


son1=Cancion("1/100","Waiting for love.mp3")
son2=Cancion("2/100","Consejos de Amor.mp3")
son3=Cancion("3/100","Me rehuso.mp3")
son4=Cancion("4/100","Mientes.mp3")
son5=Cancion("5/100","song1.mp3")
son6=Cancion("6/100","song2.mp3")#
son7=Cancion("7/100","song3.mp3")#
son8=Cancion("8/100","song4.mp3")#
son9=Cancion("9/100","song5.mp3")#
son10=Cancion("10/100","song6.mp3")##
son11=Cancion("11/100","song7.mp3")
son12=Cancion("12/100","song8.mp3")
son13=Cancion("13/100","song9.mp3")
son14=Cancion("14/100","song10.mp3")
son15=Cancion("15/100","song11.mp3")
son16=Cancion("16/100","song12.mp3")
son17=Cancion("17/100","song13.mp3")
son18=Cancion("18/100","song14.mp3")
son19=Cancion("19/100","song15.mp3")
son20=Cancion("20/100","song16.mp3")##
son21=Cancion("21/100","song17.mp3")
son22=Cancion("22/100","song18.mp3")##
son23=Cancion("23/100","song19.mp3")
son24=Cancion("24/100","song20.mp3")
son25=Cancion("25/100","song21.mp3")
son26=Cancion("26/100","song22.mp3")
son27=Cancion("27/100","song23.mp3")
son28=Cancion("28/100","song24.mp3")
son29=Cancion("29/100","song25.mp3")
son30=Cancion("30/100","song26.mp3")
son31=Cancion("31/100","song27.mp3")
son32=Cancion("32/100","song28.mp3")
son33=Cancion("33/100","song29.mp3")
son34=Cancion("34/100","song30.mp3")
son35=Cancion("35/100","song31.mp3")
son36=Cancion("36/100","song32.mp3")
son37=Cancion("37/100","song33.mp3")
son38=Cancion("38/100","song34.mp3")
son39=Cancion("39/100","song35.mp3")
son40=Cancion("40/100","song36.mp3")
son41=Cancion("41/100","song37.mp3")
son42=Cancion("42/100","song38.mp3")
son43=Cancion("43/100","song39.mp3")
son44=Cancion("44/100","song40.mp3")
son45=Cancion("45/100","song41.mp3")
son46=Cancion("46/100","song42.mp3")
son47=Cancion("47/100","song43.mp3")
son48=Cancion("48/100","song44.mp3")
son49=Cancion("49/100","song45.mp3")
son50=Cancion("50/100","song46.mp3")
son51=Cancion("51/100","song47.mp3")
son52=Cancion("52/100","song48.mp3")
son53=Cancion("53/100","song49.mp3")
son54=Cancion("54/100","song50.mp3")
son55=Cancion("55/100","song51.mp3")
son56=Cancion("56/100","song52.mp3")
son57=Cancion("57/100","song53.mp3")
son58=Cancion("58/100","song54.mp3")
son59=Cancion("59/100","song55.mp3")
son60=Cancion("60/100","song56.mp3")
son61=Cancion("61/100","song57.mp3")
son62=Cancion("62/100","song58.mp3")
son63=Cancion("63/100","song59.mp3")
son64=Cancion("64/100","song60.mp3")
son65=Cancion("65/100","song61.mp3")
son66=Cancion("66/100","song62.mp3")
son67=Cancion("67/100","song63.mp3")
son68=Cancion("68/100","song64.mp3")
son69=Cancion("69/100","song65.mp3")
son70=Cancion("70/100","song66.mp3")
son71=Cancion("71/100","song67.mp3")
son72=Cancion("72/100","song68.mp3")
son73=Cancion("73/100","song69.mp3")
son74=Cancion("74/100","song70.mp3")
son75=Cancion("75/100","song71.mp3")
son76=Cancion("76/100","song72.mp3")
son77=Cancion("77/100","song73.mp3")
son78=Cancion("78/100","song74.mp3")
son79=Cancion("79/100","song75.mp3")
son80=Cancion("80/100","song76.mp3")
son81=Cancion("81/100","song77.mp3")
son82=Cancion("82/100","song78.mp3")
son83=Cancion("83/100","song79.mp3")
son84=Cancion("84/100","song80.mp3")
son85=Cancion("85/100","song81.mp3")
son86=Cancion("86/100","song82.mp3")
son87=Cancion("87/100","song83.mp3")
son88=Cancion("88/100","song84.mp3")
son89=Cancion("89/100","song85.mp3")
son90=Cancion("90/100","song86.mp3")
son91=Cancion("91/100","song87.mp3")
son92=Cancion("92/100","song88.mp3")
son93=Cancion("93/100","song89.mp3")
son94=Cancion("94/100","song90.mp3")
son95=Cancion("95/100","song91.mp3")
son96=Cancion("96/100","song92.mp3")
son97=Cancion("97/100","song93.mp3")
son98=Cancion("98/100","song94.mp3")
son99=Cancion("99/100","song95.mp3")
son100=Cancion("100/100","song96.mp3")


son=[son1,son2,son3,son4,son5,son6,son7,son8,son9,son10,
     son11,son12,son13,son14,son15,son16,son17,son18,son19,son20,
     son21,son22,son23,son24,son25,son26,son27,son28,son29,son30
     ,son31,son32,son33,son34,son35,son36,son37,son38,son39,son40,
     son41,son42,son43,son44,son45,son46,son47,son48,son49,son50,
     son51,son52,son53,son54,son55,son56,son57,son58,son59,son60,
     son61,son62,son63,son64,son65,son66,son67,son68,son69,son70,
     son71,son72,son73,son74,son75,son76,son77,son78,son79,son80,
     son81,son82,son83,son84,son85,son86,son87,son88,son89,son90,
     son91,son92,son93,son94,son95,son96,son97,son98,son99,son100,]


#print(son3.nombre,son1.artista , son1.año)
#print(son4.nombre,son1.artista , son1.año)
#print(son5.nombre,son1.artista , son1.año)

def imprimir(a,b,c,d):
    image = Image.new('1',(128,64))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.text((15, 5),"Cancion", font=font2, fill=255)
    draw.text((60, 5),a, font=font2, fill=255)
    draw.text((15, 15),b, font=font2, fill=255)
    draw.text((15, 25),c, font=font2, fill=255)
    draw.text((15, 35),d, font=font2, fill=255)
    display.image(image)
    display.show()

def update_state():
    global state , current_time , m , s ,pos_time
    pos_time = pygame.mixer.music.get_pos()

    #print(pos_time)
    s = pos_time // 1000
    m, s = divmod(s, 60)
    m, s = int(m), int(s)

def serial():
    global x2
    x2=ser.readline()
    x2=str(x2)
    x2=x2.split("\\r\\n")
    x2=x2[0].split("b")
    x2=str(x2[1])
    x2=str(x2[1])





class Ui_MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    r=1
    def imprimir3(self):

        self.listWidget.clear()
        for r in range(101):
            x=""
            y=""
            z=""
            datos= eyed3.load(son[r-1].archivo)
            x= son[r-1].num
            y= str(datos.tag.title)
            z= str(datos.tag.artist)
            w= str(datos.tag.album)
            m= "  "
            q= x+m+y+m+z+m+w
            pos=0
            self.listWidget.insertItem(r,q)
            pos += 1
    def act(self):
        global m,s ,pos_time,lin,x,z,x3,x2,var,x4,x5
        update_state()
        self.label_2.setText(f"{m:02}:{s:02}")

        audio = mutagen.File(son[i-1].archivo)
        total_length = audio.info.length
        tm, ts = divmod(total_length+10, 60)
        tm, ts = int(tm), int(ts)
        self.label_3.setText(f"{tm:02}:{ts:02}")
        #print(total_length)

        self.sl.setMinimum(0)
        self.sl.setMaximum(total_length)
        self.sl.setValue(pos_time/1000)
        #print(total_length)
        #print(pos_time/1000)

        serial()


        if (x2=="1" or x2=="2" or x2=="0" or x2=="3"or
            x2=="4" or x2=="5" or x2=="6" or x2=="7" or
            x2=="8" or x2=="9"):
            if (x3==""):
                x3=x2
                x5=1
                x4=0

            elif(x3!=""and x5==1 and x4<=3):
                x3=x3+x2
                var=1
            print(x3)

        if (x4==2 and x3!=""):
            x=int(x3)
            print("iniciando cancion")
            self.actualizar()
            x5=0

        elif(x2=="B"):
            print("siguiente")
            self.siguiente()
        elif(x2=="C"):
            print("reiniciar")
            self.reiniciar()
        elif(x2=="A"):
            print("aleatorio")
            self.aleatorio()
        elif(x2=="#"):
            print("anterior")
            self.anterior()
        elif(x2=="*"):
            print("pausa")
            self.pausa()
        elif(x2=="D"):
            print("unpausa")
            self.unpausa()




        x4+=1
        if (x4==3):
            x4=0
            x3=""


        sel=self.pushButton_5.setCheckable(True)
        #print(sel)
        if (pos_time/1000 >= total_length+10):
            print(2)
            #sel=self.pushButton_5.isChecked()
           # print(sel)
            if (self.pushButton_5.isChecked()):
                x=random.randint(1,100)
                print(x)
                #print("holaaaaaaaaaa")
                z=1
                self.actualizar()
            else:
                print(3)
                self.siguiente()




    def __init__(self, *args, **kwargs):
        global i

        self.timer=QtCore.QTimer()
        self.timer.timeout.connect(self.act)
        self.timer.start(300)

        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.actualizar)
        self.pushButton_2.clicked.connect(self.siguiente)
        self.pushButton_3.clicked.connect(self.pausa)
        self.pushButton_4.clicked.connect(self.anterior)
        self.pushButton_5.clicked.connect(self.aleatorio)
        self.pushButton_6.clicked.connect(self.reiniciar)
        self.pushButton_7.clicked.connect(self.unpausa)
        self.imprimir3()
        self.sl = self.horizontalSlider





        #draw.text((30, 32), "Bienvenido", font=font3, fill=255)
        #display.image(image)
        #display.show()





    def actualizar(self):
        global x,i,lin1,a,b,c,d,current_time,m,s,z

        i=0
        lin1=self.lineEdit.text()
        if(lin1==''):
            if x>0 and lin1!=x :
                lin1=str(x)
                #print(x)
                lin1=int(lin1)
            for i in range(lin1):
                i=i+1


        elif(lin1!=int):
            lin1=int(lin1)
            if x>0 and lin1!=x and z==1:
                lin1=str(x)
                print(x)
                lin1=int(lin1)
            for i in range(lin1):
                i=i+1



        def imprimir2(a,b,c,d):
            self.listWidget_2.clear()
            for j in range(1):
                pos=0
                self.listWidget_2.insertItem(j,a)
                pos += 1
                self.listWidget_2.insertItem(j,b)
                pos += 1
                self.listWidget_2.insertItem(j,c)
                pos += 1
                self.listWidget_2.insertItem(j,d)



        def iniciar():
            global x,i,lin1,a,b,c,d,e,z
            print(i)
            pygame.mixer.music.load(son[i-1].archivo)
            pygame.mixer.music.play(0)
            datos= eyed3.load(son[i-1].archivo)
            a=son[i-1].num
            b= str(datos.tag.title)
            c= str(datos.tag.artist)
            d= str(datos.tag.album)
            imprimir2(a,b,c,d)
            imprimir(a,b,c,d)
            print(a,b,c,d)
            z=0




        iniciar()

    def pausa(self):
            pygame.mixer.music.pause()



    def siguiente(self):
        global lin1,x,z
        x=int(lin1)
        x=x+1
        z=1

        self.actualizar()


    def anterior(self):

        global lin1,x,z
        x=int(lin1)
        x=x-1
        z=1
        self.actualizar()


    def reiniciar(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.play()

    def aleatorio(self):
        print("aleatorio")
        x=random.randint(1,100)
        self.actualizar()


    def unpausa(self):
        pygame.mixer.music.unpause()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Ui_MainWindow()
    window.show()

    app.exec_()
