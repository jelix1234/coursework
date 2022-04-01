# the below code is meant to draw a cheese board shape with the colour black and red 
# import turtle package
import turtle 
   
# create screen object
sc = turtle.Screen()
   
#turtle object creation
pen = turtle.Turtle()
   
# draw square
def draw():
   
  for i in range(4):
    pen.forward(30)
    pen.left(90)
   
  pen.forward(30)
   
# main Code
if __name__ == "__main__" :
      
    # set screen
    sc.setup(600, 600)
       
    # speed set to 100,but could be change to 0 if needed to be faster 
    pen.speed(100)
       
    # the loop for the board,number of occurance
    for i in range(8):
       
      # 
      pen.up()
       
      # set position for every row
      pen.setpos(0, 30 * i)
       
      # ready to draw
      pen.down()
       
      # row
      for j in range(8):
       
        # conditions for alternative color,which can be change to any other colour the user want
        if (i + j)% 2 == 0:
          col ='black'
       
        else:
          col ='red'
       
        # fill with given color inputed 
        pen.fillcolor(col)
       
        # start filling with colour
        pen.begin_fill()
       
        # call method
        draw()
        # stop filling with colours 
        pen.end_fill()
       
    # hide the turtle
    pen.hideturtle()
       
    # idea gotten from www.geeksforgeeks.org
    
