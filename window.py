import tkinter

class Window:
    def __init__(self,width,height) -> None:
        self.__master = tkinter.Tk()
        self.__master.title("Maze Solver :)")
        self.__master.protocol("WM_DELETE_WINDOW",self.close)
        self.__canvas = tkinter.Canvas(self.__master,width=width,height=height,bg="black")
        self.__canvas.pack(fill="both")
        self.__is_running = False
    
    def redraw(self):
        self.__master.update_idletasks()
        self.__master.update()
    
    def wait_for_close(self):
        self.__is_running=True
        while self.__is_running:
            self.redraw()
    
    def close(self):
        self.__is_running=False

    def draw_line(self,line,color="green"):
        line.draw(self.__canvas,color)

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Line:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def draw(self,canvas,color="white"):
        canvas.create_line(self.start.x,self.start.y,self.end.x,self.end.y,fill=color)

