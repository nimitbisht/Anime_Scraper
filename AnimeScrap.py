from tkinter import *
from PIL import ImageTk, Image
from tkinter import StringVar, ttk
from tkinter import filedialog
import requests
from bs4 import BeautifulSoup
import os

link = []
number=[]

def Search_anime(): 
    textb.configure(state='normal')
    textb.delete(1.0,END)
    if len(e1.get()) != 0:
        anime_name = e1.get()
        search_url = ("https://gogoanime2.org/search/" + anime_name)

        html1 = requests.get(search_url).content
        soup = BeautifulSoup(html1,"html.parser")

        #get details(soup)
        title = []
        result = []
        raw_soup = soup.find_all('div', {"class":'img'})
        link.clear()
        for item in raw_soup:
            temp_soup = item.find('a')
            title.append(temp_soup['title'])
            link.append(temp_soup['href'])

        #Create(title,link)
        for i in range(len(title)):
            result.append(f"{i+1} : {title[i]} \n")
        textb.insert(1.0,result)
        textb.configure(state='disabled')

def description():
    textb.configure(state='normal')
    textb.delete(1.0,END)
    i = int(e2.get())
    source_code = requests.get("https://gogoanime2.org/%s" % (link[i-1]))
    content = source_code.content
    soup = BeautifulSoup(content,'html.parser')
    container_soup = soup.find('div', {'class':'anime_info_body_bg'})
    titles_detail = container_soup.find_all('p',{'class':'type'})

    discription = []
    for elem in titles_detail:
        discription.append(elem.getText())
    textb.insert(1.0,discription)
    textb.configure(state='disabled')
    ep_link = []
    ul = soup.find("div",class_="anime_video_body")

    for a in ul.find_all('a',href=True):
        ep_link.append("https://gogoanime2.org/"+ a['href'])
    number = len(ep_link)
    print("Totla episodes " + str(number))
    print(ep_link)
    print("\n")
  


root = Tk()
root.resizable(0,0)
root.geometry("600x670")
root.title("BULK ANIME DOWNLOADER")
# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Set the iconbitmap using the relative path
icon_path = os.path.join(current_directory, 'icons\icon.ico')
root.iconbitmap(icon_path)
# root.iconbitmap('D:\python\icon.ico')
root.config(background="#C9CCD5")
root.columnconfigure(0,weight=1)

# Anime Downloader (IMAGE)

image_path = os.path.join(current_directory, 'icons\pok.jpg')
image = Image.open(image_path)

# image=Image.open("D:\python\pok.jpg")
image = image.resize((600, 130))
photo=ImageTk.PhotoImage(image)
l1 = Label(image=photo)                          
l1.grid(row=0,column=0)                    

#FRAME 0(BASE frame)
f0 = Frame(root,bg='#3E2C41',borderwidth=0)
f0.grid()
#FRAME 1
f1 = Frame(f0,bg='white',borderwidth=7)
f1.grid(row=0,column=0)
#FRAME 2
f2 = Frame(f0,borderwidth=10,bg="#464660")
f2.grid(row=3,column=0)
#FRAME 3
f3 = Frame(f0,borderwidth=10,bg="#3E2C41")
f3.grid(row=4,column=0)
#FRAME 4
f4 = Frame(f0,borderwidth=10,bg="#3E2C41")
f4.grid(row=5,column=0)
#Frame 5
f5 = Frame(f0,borderwidth=10,bg="#11052C")
f5.grid(row=6,column=0)


#f1
l1 = Label(f1, text = "Search Anime : ",font="Raleway",fg="#261C2C",bg="white")
l1.grid(row=0,column=0)

evar = StringVar()
e1 = Entry(f1,width=38,textvariable=evar,font=("times new roman ", 15),bg="lightgray")
e1.grid(row=0,column=1)

button0 = Button(f1,text="SEARCH",command=Search_anime,bg='#FFB319',fg='white',activebackground="#6B7AA1",font=("times new roman ", 15),bd=1)
button0.grid(columnspan=3)


#f2
textb = Text(f2,height=10,width=50,padx=15,pady=15,bg="#E8D0B3")
textb.grid(row=0,column=0,ipadx=70)

e2 = Entry(f2,width=7,bg="lightgray")
e2.grid()

l2 =Label(f2, text = "Select",font=("Impack 15 bold"),fg="#FFE6E6",bg="#464660")
l2.grid()

#f3

#f4
button2 = Button(f4,text="WATCH",bg='#2D46B9',fg='white',activebackground="#6B7AA1",font=("times new roman ", 15),bd=1,height=2,width=15,command=description)
button2.grid()

#f5
labelf5 = Label(f5,text="Copy link from terminal and open in browser ",fg="#261C2C",font=("times new roman ", 15))
labelf5.grid(row=2,column=2)


root.mainloop()
