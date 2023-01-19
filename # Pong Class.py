# Pong Class
import turtle


class pong:
  # Pat
  

  #Rik
  
  
  # is it possible to do it like this? :
  
    

  def blocky(self, paddle, c, xval):
    paddle = turtle.Turtle(shape= 'square')
    paddle.setx(xval)
    paddle.speed(0)
    paddle.color(c)
    paddle.resizemode("user")
    paddle.shapesize(stretch_wid =6, stretch_len =1)
    

    

  def rblock(self):
    rblock = self.rblock()
    return self.blocky(rblock, "red", 400)

  def lblock(self):
    lblock = self.lblock()
    return self.blocky(lblock, "blue", -400)

  





    




  #Pat
  #def ball(self):
  
  #Pat
  def board(self):
    board = turtle.Screen()
    board.title("Pong by Pat and Rik")
    board.bgcolor("gray")
    board.setup(width=1000, height=600)
    

  def play(self):
    while True:
        self.board()
        self.lblock()
        self.rblock()

pong = pong()
pong.play()