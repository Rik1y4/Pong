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
    rb.color("black")
    rb.shapesize(stretch_wid=5, stretch_len=1)
    rb.penup()
    rb.goto(480, 0)

    lb = t.Turtle()
    lb.shape(name="square")
    lb.resizemode("user")
    lb.color("black")
    lb.shapesize(stretch_wid=5, stretch_len=1)
    lb.penup()
    lb.goto(-480, 0)

    ball = t.Turtle()
    ball.shape(name="circle")
    ball.color("white")
    ball.penup()
    ball.dx = 2
    ball.dy = 2

    score1 = 0
    score2 = 0

    pen = t.Turtle()
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 350)
    pen.write("Player1:"+str(score1)+"  Player2:"+str(score2), align= "center", font=("Courier", 24, "normal"))

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
                self.score1+=1
                self.pen.clear()
                self.pen.write("Player1:"+str(self.score1)+"  Player2:"+str(self.score2), align= "center", font=("Courier", 24, "normal"))
                

            if self.ball.xcor() < -490:
                self.ball.setx(-490)
                self.ball.dx*=-1
                self.score2+=1
                self.pen.clear()
                self.pen.write("Player1:"+str(self.score1)+"  Player2:"+str(self.score2), align= "center", font=("Courier", 24, "normal"))



            if self.ball.xcor()> 460 and self.ball.xcor()< 490 and (self.ball.ycor() < self.rb.ycor()+50 and self.ball.ycor()> self.rb.ycor()-50):
                self.ball.dx*=-1
            

            if self.ball.xcor()< -460 and self.ball.xcor()> -490 and (self.ball.ycor()< self.lb.ycor()+ 50 and self.ball.ycor()> self.lb.ycor()-50):
                self.ball.dx*=-1
    

        
    

            

pong = pong()   
pong.play()

    