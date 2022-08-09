import requests
import tkinter as tk
from datetime import datetime

canvas = tk.Tk()
canvas.geometry("400x300")
canvas.title("Bitcoin Tracker")
canvas["bg"] = "light yellow"

f1=("poppins",24,"bold")
f2=("poppins",22,"bold")
f3=("poppins",18,"normal")

def trackBitcoin():
    url="https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,INR,CAD"
    response=requests.get(url).json()
    price = response["USD"]
    
    time=datetime.now().strftime("%H:%M:%S")
    
    labelPrice.config( text = str(price) + "$")
    labelTime.config(text = "Update at :" + time)

label=tk.Label(canvas, text="Bitcoin Tracker",font=f1,fg = "Dark goldenrod" ,bg = "light yellow")
label.pack(pady = 20)

labelPrice=tk.Label(canvas,font = f2,fg = "Dark goldenrod" ,bg = "light yellow")
labelPrice.pack(pady = 20)

labelTime=tk.Label(canvas,font = f3, fg = "Dark goldenrod" , bg = "light yellow")
labelTime.pack(pady = 20)

trackBitcoin()
canvas.mainloop()