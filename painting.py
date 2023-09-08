import tkinter as tk

window=tk.Tk()
window.geometry('300x300')
window.title('Paint')

paint=tk.Canvas(window,bg='white')
paint.pack()

def draw_on_canvas(event):
    x=event.x
    y=event.y
    paint.create_oval((x - brush_size /2 ,y - brush_size /2,x + brush_size /2,y + brush_size /2),fill = 'black')
def brush_size_adjust(event):
    global brush_size
    if event.delta > 0 :
        brush_size +=4
    else:
        brush_size -= 4
    brush_size = max(0 ,min(brush_size,50))
brush_size = 2
paint.bind('<Motion>',draw_on_canvas)
paint.bind('<MouseWheel>',brush_size_adjust)








window.mainloop()
