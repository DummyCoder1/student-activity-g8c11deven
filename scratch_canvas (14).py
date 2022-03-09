import turtle , random


l1=[10,20,30,40,50,60,70,80,90,100,120,130]
c1=["blue","red","green","cyan","purple","black","brown","pink","orange","yellow","grey"]
def draw_arrow(l,c):
    for value in l:
        turtle.forward(value)
        turtle.pencolor(random.choice(c))
        turtle.stamp()
        turtle.backward(value)
        turtle.right(30)
        l.append(value+20)
        l.remove(value)
        print(l)
        
draw_arrow(l1,c1)        








