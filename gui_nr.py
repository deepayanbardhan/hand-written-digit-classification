from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import cv2
from tkinter.messagebox import showerror
from image_process import find_num, crop
from tensorflow.keras.models import load_model
import numpy as np

root = Tk()
root.title('Hand written Digit Classifier')
model = load_model('d:/deepayan/study/Coding/kaggle/digit-recognizer/my_model_1.h5')

def from_image():
    global flag
    global cap

    cap.release()
    cv2.destroyAllWindows()
    flag = 0
    global img
    root.filename = filedialog.askopenfilename(initialdir="D:/deepayan/study/coding/Kaggle/digit-recognizer", title="Select a File",filetypes=(("jpg files","*.jpg"),("all files","*.*")))
    img = cv2.imread(root.filename)
    marked_img, bbox = find_num(img)
    number_img = crop(img, bbox)
    
    img = Image.fromarray(cv2.resize(marked_img,(200,200)))
    imgtk = ImageTk.PhotoImage(image=img)
    l1.imgtk = imgtk
    l1.configure(width=200, height=200, image=imgtk)
    img2 = Image.fromarray(cv2.resize(number_img,(200,200)))
    imgtk = ImageTk.PhotoImage(image=img2)
    l2.imgtk = imgtk
    l2.configure(width=200, height=200, image=imgtk)
    im = np.reshape(number_img, (1,28,28,1))
    prediction = model.predict_classes(im)
    t4.config(text=str(prediction), width = 20)

def from_video(k):
    global flag
    global cap
    flag=k
    if flag==0:
        return
    if flag==1:
        flag=flag+1
        cap = cv2.VideoCapture(0)

    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    marked_img, bbox = find_num(cv2image)
    number_img = crop(cv2image, bbox)
    im = np.reshape(number_img, (1,28,28,1))
    prediction = model.predict_classes(im)
    t4.config(text=str(prediction), width = 20)

    img = Image.fromarray(cv2.resize(cv2image,(200,200)))
    imgtk = ImageTk.PhotoImage(image=img)
    l1.imgtk = imgtk
    l1.configure(width=200, height=200, image=imgtk)
    img2 = Image.fromarray(cv2.resize(number_img,(200,200)))
    imgtk = ImageTk.PhotoImage(image=img2)
    l2.imgtk = imgtk
    l2.configure(width=200, height=200, image=imgtk)
    l2.after(10, lambda: from_video(flag)) 

app = LabelFrame(root, height=400,width=500)
app.grid_propagate(0)
app.pack()
b1 = Button(app, text = "load image", padx=2, pady=2, command=from_image,width=20)
b2 = Button(app, text = "Live classify", padx=2, pady=2, command=lambda: from_video(1), width=20)
l1 = Label(app, padx=10, pady=10, width=25, height=12, borderwidth = 4, relief='sunken')
l2 = Label(app, padx=10, pady=10, width=25, height=12, borderwidth = 4, relief='sunken')
t1 = Label(app, text="Area under Concideration", width = 20)
t2 = Label(app, text="Input to the model", width = 20)
t3 = Label(app, text="Prediction result   : : : ", width = 30)
t4 = Label(app, text="", width = 5)

b1.place(x=180, y=5)
b2.place(x=180, y=35)
l1.place(x=30, y=80)
l2.place(x=250,y=80)
t1.place(x=60, y=290)
t2.place(x=280, y=290)
t3.place(x=80, y=350)
t4.place(x=250, y=350)

cap = cv2.VideoCapture(0)

root.mainloop()