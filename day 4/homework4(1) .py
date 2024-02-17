from turtle import *

speed(100)
width(5)
color("green")
begin_fill()

#making grass 

forward(410)
left(180)
forward(830)
left(90)
forward(380)
left(90)
forward(830)
left(90)
forward(380)
end_fill()

#making houses


left(90)
forward(250)

color("blue")

begin_fill()

right(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)

end_fill()

#making roof

left(90)
forward(100)

color("yellow")
begin_fill()
left(30)
forward(100)
left(120)
forward(100)
left(30)
left(90)
forward(100)
end_fill()

#making a door

color("blue")

right(90)
forward(100)
right(90)
forward(40)

color("black")
begin_fill()
right(90)
forward(40)
left(90)
forward(20)
left(90)
forward(40)
left(90)
forward(20)
end_fill()


left(180)
forward(25)

color("blue")
forward(40)

color("green")

forward(200)
right(90)

#house 2

color("blue")

begin_fill()

right(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)

end_fill()

#roof 2

left(90)
forward(100)

left(90)
forward(100)

color("yellow")
begin_fill()
left(30)
forward(100)
left(120)
forward(100)
left(30)
left(90)
forward(100)
end_fill()

color("blue")
right(90)
forward(100)
right(90)
forward(40)

color("black")
begin_fill()
right(90)
forward(40)
left(90)
forward(20)
left(90)
forward(40)
left(90)
forward(20)
end_fill()

left(180)
forward(25)
color("blue")
forward(40)
color("green")
forward(270)
right(90)

#making sky

color("cyan")
begin_fill()
forward(390)
right(90)
forward(830)
right(90)
forward(390)
right(90)
forward(250)
right(90)
forward(100)
left(30)
forward(100)
left(120)
forward(100)
left(30)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
left(30)
forward(105)
left(120)
forward(105)
left(30)
forward(100)
right(90)
forward(280)
end_fill()

#making sun

right(90)
right(20)
color("cyan")
forward(350)

begin_fill()
color("yellow")
circle(50)
end_fill()

#"escaping sun"

right(70)

forward(1)
color("cyan")


forward(100)

#stars

color("white")
begin_fill()
forward(20)
left(70)
forward(20)
right(140)
forward(20)
left(70)
forward(20)
right(150)
forward(20)
left(90)
forward(20)
right(150) 
forward(20)
left(70)
forward(20)
right(140)
forward(20)
left(70)
forward(20)
end_fill()

color("cyan")
forward(50)


color("white")
begin_fill()
forward(20)
left(70)
forward(20)
right(140)
forward(20)
left(70)
forward(20)
right(150)
forward(20)
left(90)
forward(20)
right(150) 
forward(20)
left(70)
forward(20)
right(140)
forward(20)
left(70)
forward(20)
end_fill()

right(30)

color("cyan")
forward(50)
color("white")
begin_fill()
forward(20)
left(70)
forward(20)
right(140)
forward(20)
left(70)
forward(20)
right(150)
forward(20)
left(90)
forward(20)
right(150) 
forward(20)
left(70)
forward(20)
right(140)
forward(20)
left(70)
forward(20)
end_fill()






#homework done easy peasy lemon squasy

exitonclick()