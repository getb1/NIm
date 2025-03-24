import tkinter as tk
from tkinter import font as tkFont
import random

class Stone:

    def __init__(self,x,y,canvas):
        self.image = tk.PhotoImage(file="/home/pi/Nim/New Piskel-1.png").zoom(2,2)
        self.centre_x = x
        self.centre_y = y
        self.canvas = canvas

        self.sprite = self.canvas.create_image(x,y,image=self.image)
        
    
    def hide_stone(self):
        pass

    def show_stone(self):
        pass

    def redraw_stone(self, new_x=-1, new_y=-1):

        if new_x<-1 and new_y<-1:

            return
        self.canvas.delete(self.sprite)
        self.sprite = self.canvas.create_image(new_x,new_y,image=self.image)
    
    def coordinates(self):
        return self.centre_x,self.centre_y




    


class Pile:

    def __init__(self,stones:int,start_pos:tuple,the_canvas):

        self.num_stones = stones
        self.start_pos = start_pos
        self.canvas = the_canvas
        self.stones = [Stone(start_pos[0]+i*100,start_pos[1], the_canvas) for i in range(stones)]
    
    def __len__(self):
        return self.num_stones

    def draw(self,new_start_pos=None):

        self.start_pos = new_start_pos if new_start_pos is not None else self.start_pos
        for i,stone in enumerate(self.stones):
            
            stone.redraw_stone(self.start_pos[0]+i*100,self.start_pos[1])

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
        self.stones = self.create_piles()
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

    def within_circle(self,x,y,cx,cy,radius):

        return (((x-cx)**2 + (y-cy)**2)**0.5)<radius

    def mouseClicked(self,e):
        self.theCanvas.delete(self.clickText)
        self.clickText = self.theCanvas.create_text(750,20, text=f"Clicked at {e.x}, {e.y}", anchor="ne")

        x = e.x
        y = e.y

        for i,pile in enumerate(self.stones):
            for j,stone in enumerate(pile.stones):
                cx,cy=stone.coordinates()

                if self.within_circle(x,y,cx,cy,32):
                    print(i,j)

    def canvasButtonClicked(self,e):
        self.theCanvas.itemconfigure(self.canvasbutton,image=self.clicked )
        self.after(1000,self.restorebutton)

    def restorebutton(self):
        self.theCanvas.itemconfigure(self.canvasbutton,image=self.buttonPic )
    
    def create_piles(self):

        new=[]

        sizes = [7,5,3,1]

        for i in range(len(sizes)):
            new.append(Pile(sizes[i],(100+50*(7-sizes[i]),625-100*i),self.theCanvas))

        return new

    def redraw_piles(self):

        sizes = [len(p) for p in self.piles]

        for i in range(len(sizes)):
            self.stones[i]=Pile(sizes[i],(100+50*(7-sizes[i]),625-100*i),self.theCanvas)


    


app = Main()


        
