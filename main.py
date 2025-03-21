import tkinter as tk
from tkinter import font as tkFont
import random

class Stone:

    def __init__(self,x,y,canvas):
        self.image = tk.PhotoImage(file="/home/pi/Nim/New Piskel-1.png").zoom(2,2)
        self.centre_x = x
        self.centre_y = y
        self.canvas = canvas

        self.canvas.create_image(x,y,image=self.image)
        
    
    def hide_stone(self):
        pass

    def show_stone(self):
        pass

    


class Pile:

    def __init__(self,stones:int,start_pos:tuple,the_canvas):

        self.num_stones = stones
        self.start_pos = start_pos
        self.canvas = the_canvas
        self.stones = [Stone(start_pos[0]+i*100,start_pos[1], the_canvas) for i in range(stones)]
    
    def __len__(self):
        return self.num_stones

    def draw(self):
        tk.PhotoImage(file=self.image)

    def remove_stone(self):
        pass
        

class Main(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #Setup
        


        self.geometry("950x900+0+0")
        self.theCanvas = tk.Canvas(self,width=800, height=900, bg="#ffffff")
        self.theCanvas.grid(row=0, column=0)
        self.buttonfont = tkFont.Font(family="Consolas", weight="bold")
        self.stones = [Pile(7,(70,600),self.theCanvas)]
        self.button1 = tk.Button(self, text="Normal Button", font=self.buttonfont, command = self.buttonClicked)
        self.button1.grid(row=0, column=1)

        self.theCanvas.bind("<Motion>", self.mouseMoved)
        self.theCanvas.bind("<Button-1>", self.mouseClicked)

        self.buttonPic = tk.PhotoImage(file="button.png")
        self.clicked = tk.PhotoImage(file="click.png")
        
        self.canvasbutton = self.theCanvas.create_image(200,800,image = self.buttonPic)
        self.theCanvas.tag_bind(self.canvasbutton, "<Button-1>", self.canvasButtonClicked)
        
        self.movetext=None
        self.clickText = None
        self.buttonText = None
        self.mainloop()


    def buttonClicked(self):
        x = random.randint(100,700)
        y = random.randint(100,700)
        self.theCanvas.delete(self.buttonText)
        self.buttonText = self.theCanvas.create_text(x,y,text="tkinter Button clicked")

    def mouseMoved(self,e):
        self.theCanvas.delete(self.movetext)
        self.movetext = self.theCanvas.create_text(20,20, text=f"moved to {e.x}, {e.y}", anchor="nw")

    def mouseClicked(self,e):
        self.theCanvas.delete(self.clickText)
        self.clickText = self.theCanvas.create_text(750,20, text=f"Clicked at {e.x}, {e.y}", anchor="ne")

    def canvasButtonClicked(self,e):
        self.theCanvas.itemconfigure(self.canvasbutton,image=self.clicked )
        self.after(1000,self.restorebutton)

    def restorebutton(self):
        self.theCanvas.itemconfigure(self.canvasbutton,image=self.buttonPic )
    
    def draw_stones(self):
        pass


app = Main()


        
