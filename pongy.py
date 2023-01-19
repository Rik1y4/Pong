import turtle as t

class pong:

    gs = t.Screen()
    gs.setup(width=1000, height=800)
    gs.bgcolor("gray")
    gs.title("Pong by Pat and Rik")
    gs.tracer(0)

    rb = t.Turtle()
    rb.shape(name="square")
    rb.resizemode("user")
    rb.color("blue")
    rb.shapesize(stretch_wid=4, stretch_len=2)
    rb.penup()
    rb.goto(400, 0)

    lb = t.Turtle()
    lb.shape(name="square")
    lb.resizemode("user")
    lb.color("red")
    lb.shapesize(stretch_wid=4, stretch_len=2)
    lb.penup()
    lb.goto(-400, 0)

    ball = t.Turtle()
    ball.shape(name="circle")
    ball.color("white")
    ball.penup()
    ball.dx = 2
    ball.dy = 2

    def resetball():
        pong.ball.setposition(0,0)
    
    

    def rup():
        y= pong.rb.ycor()
        y+=30
        pong.rb.sety(y)

    def rdow():
        y= pong.rb.ycor()
        y-=30
        pong.rb.sety(y)

    def lup():
        y= pong.lb.ycor()
        y+=30
        pong.lb.sety(y)

    def ldow():
        y= pong.lb.ycor()
        y-=30
        pong.lb.sety(y)


    gs.listen()
    gs.onkeypress(lup, "w")
    gs.onkeypress(ldow, "s")
    gs.onkeypress(rup, "Up")
    gs.onkeypress(rdow, "Down")
    gs.onkeypress(resetball, "f")
    

    def play(self):
        while True:
            self.gs.update()

            xe = self.ball.xcor() + self.ball.dx
            ye = self.ball.ycor() + self.ball.dy
            self.ball.setposition(xe, ye)

            if self.ball.ycor() > 390:
                self.ball.sety(390)
                self.ball.dy*=-1

            if self.ball.ycor() < -390:
                self.ball.sety(-390)
                self.ball.dy*=-1

            if self.ball.xcor() > 490:
                self.ball.setx(490)
                self.ball.dx*=-1

            if self.ball.xcor() < -490:
                self.ball.setx(-490)
                self.ball.dx*=-1

    

        
    

            

pong = pong()   
pong.play()

    