from datetime import datetime
from tqdm import tqdm
import requests
import re
import sys
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import webbrowser

def callback(event):
    webbrowser.open_new(event.widget.cget("text"))

def call():
    res = mb.askquestion('Exit Application', 
                         'Do you really want to exit')
      
    if res == 'yes' :
        root.destroy()
          
    else :
        mb.showinfo('Return', 'Returning to Login Box')
  
root = tk.Tk()
root.title("Login Instagram Box")

lb1 = tk.Button(root, text = "Welcome", font=("Algerian", 21, "bold"), fg = "yellow", bg = "red")
lb1.pack()

lb2 = tk.Label(root, text = "Hey Folk, please click here to login to Instagram and proceed!!", font = ("Monotype Corsiva", 25, "bold"), fg = "green")
lb2.pack()

lb3 = tk.Label(root, text = "http://www.instagram.com", font = ("Algerian", 25, "bold"), fg="blue", cursor="hand2")
lb3.pack()
lb3.bind("<Button-1>", callback)

lb4 = tk.Label(root, text = "Please quit application if already logged in and proceed!!", font = ("Monotype Corsiva", 25, "bold"), fg = "green")
lb4.pack()

lb5 = tk.Button(root, text = 'Quit Application', font = ("Algerian", 21, "bold"), fg = "yellow", bg = "red", command=call)
lb5.pack()

root.mainloop()


print('''

                        [WELCOME TO INSTASTORE]\n        [PRESENTING THE INSTAGRAM PHOTO AND VIDEO DOWNLOADER]              
                        
''')                ##  Heading

##  Function to check the Internet Connection
def internet(url='https://www.google.com/', timeout=5):
    try:
        req = requests.get(url, timeout=timeout)
        req.raise_for_status()
        print("You're connected to Internet successfully. You can proceed to your work!!\n")
        return True
    except requests.HTTPError as e: 
        print("Checking internet connection failed, status code {0}.".format(e.response.status_code))
    except requests.ConnectionError:
        print("No internet connection available. Please provide an Internet connection to proceed!!")
        input("\nPress Enter to close")
    return False

##  Function to download an Instagram Photo
def download_photo():
    
    url = input("\nPlease enter your desired Image URL from your Instagram profile: \n")
    x = re.match(r'^(https:)[/][/]www.([^/]+[.])*instagram.com', url)

    try:
        if x:
            request_image = requests.get(url)   ##  requests and get the url
            src = request_image.content.decode('utf-8')
            check_type = re.search(r'<meta name="medium" content=[\'"]?([^\'" >]+)', src)
            check_type_f = check_type.group()
            final = re.sub('<meta name="medium" content="', '', check_type_f)

            if final == "image":
                print("\nDownloading the image...")
                extract_image_link = re.search(r'meta property="og:image" content=[\'"]?([^\'" >]+)', src)
                image_link = extract_image_link.group()
                final = re.sub('meta property="og:image" content="', '', image_link)
                _response = requests.get(final).content
                file_size_request = requests.get(final, stream=True)
                file_size = int(file_size_request.headers['Content-Length'])
                block_size = 1024
                filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
                with open(filename + '.jpg', 'wb') as f:
                    for data in file_size_request.iter_content(block_size):
                        t.update(len(data))
                        f.write(data)
                t.close()
                print("\nImage downloaded successfully!!")
                print("\n          THANKS FOR VISITING!! HAVE A NICE DAY AHEAD!!\n\nKINDLY PROVIDE YOUR FEEDBACK OR CONTRIBUTIONS IN PROVIDED LINK IF INTERESTED!! ")
                print("             https://github.com/Rakesh9100/InstaStore")

        else:
            print("Entered URL is not an instagram.com URL.")
    except AttributeError:
        print("Unknown URL!!")

##  Function to download an Instagram Video
def download_video():

    url = input("\nPlease enter your desired Video URL from your Instagram profile: \n")
    x = re.match(r'^(https:)[/][/]www.([^/]+[.])*instagram.com', url)

    try:
        if x:
            request_image = requests.get(url)
            src = request_image.content.decode('utf-8')
            check_type = re.search(r'<meta name="medium" content=[\'"]?([^\'" >]+)', src)
            check_type_f = check_type.group()
            final = re.sub('<meta name="medium" content="', '', check_type_f)

            if final == "video":
                print("\nDownloading the video...")
                extract_video_link = re.search(r'meta property="og:video" content=[\'"]?([^\'" >]+)', src)
                video_link = extract_video_link.group()
                final = re.sub('meta property="og:video" content="', '', video_link)
                _response = requests.get(final).content
                file_size_request = requests.get(final, stream=True)
                file_size = int(file_size_request.headers['Content-Length'])
                block_size = 1024
                filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
                with open(filename + '.mp4', 'wb') as f:
                    for data in file_size_request.iter_content(block_size):
                        t.update(len(data))
                        f.write(data)
                t.close()
                print("\nVideo downloaded successfully!!")
                print("\n          THANKS FOR VISITING!! HAVE A NICE DAY AHEAD!!\n\nKINDLY PROVIDE YOUR FEEDBACK OR CONTRIBUTIONS IN PROVIDED LINK IF INTERESTED!! ")
                print("             https://github.com/Rakesh9100/InstaStore")
        else:
            print("Entered URL is not an instagram.com URL.")
    except AttributeError:
        print("Unknown URL!!")

## Function to download an Instagram Profile Picture
import instaloader
def download_dp():
    
    ig = instaloader.Instaloader()  # Create instance
    user = input("Please enter your Instagram Username: ")
    ig.download_profile(user, profile_pic_only = True)  # download profile
    print("\nProfile Photo downloaded successfully!!")
    print("\n          THANKS FOR VISITING!! HAVE A NICE DAY AHEAD!!\n\nKINDLY PROVIDE YOUR FEEDBACK OR CONTRIBUTIONS IN PROVIDED LINK IF INTERESTED!! ")
    print("             https://github.com/Rakesh9100/InstaStore")

if internet() == True:
    try:
        while True:
            print("Press 'A' or 'a' to download your Instagram Photo.\nPress 'B' or 'b' to download your Instagram Video. "
                  "\nPress 'C' or 'c' to download your Instagram Profile Picture.\nPress 'E' or 'e' to Exit.")
            select = str(input("\nINSTA DOWNLOADER --> "))
            try:
                if select == 'A' or select == 'a':
                    download_photo()
                    input("\nPress Enter to close ")
                if select == 'B' or select == 'b':
                    download_video()
                    input("\nPress Enter to close ")
                if select == 'C' or select == 'c':
                    download_dp()
                    input("\nPress Enter to close ")
                if select == 'E' or select == 'e':
                    print("\n          THANKS FOR VISITING!! HAVE A NICE DAY AHEAD!!\n\nKINDLY PROVIDE YOUR FEEDBACK OR CONTRIBUTIONS IN PROVIDED LINK IF INTERESTED!! ")
                    print("             https://github.com/Rakesh9100/InstaStore")
                    input("\nPress Enter to close ")
                    sys.exit()
                else:
                    sys.exit()
            except (KeyboardInterrupt):
                print("Programme Interrupted")
    except(KeyboardInterrupt):
        print("\nProgramme Interrupted")
else:
    sys.exit()
