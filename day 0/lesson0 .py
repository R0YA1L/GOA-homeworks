from turtle import * 
#we want to paint a house

shape("arrow")


#draw a square
speed(20)
width(8)

color("red")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)


forward(80)
left(90)
end_fill()


color("black")

forward(80)
right(90)

forward(50)
right(90)
forward(80)

right(90)
forward(50)

penup()
goto(200, 200)
pendown()


color("brown")
begin_fill()
right(60)
forward(200)

left(120)
forward(200)
end_fill()

color("red")


#drawing grass

left(30)
forward(200)


begin_fill()
color("green")
right(90)

forward(200)

right(180)
forward(600)


left(180)
forward(800)
left(90)
forward(350)
left(90)
forward(800)
left(90)
forward(353)
end_fill()

left(90)



#coloring door :D
forward(320)

begin_fill()

color("black")
right(90)
forward(80)

right(90)
forward(55)
right(90)
forward(80)
right(90)
forward(50)

end_fill()


#drwaing sky

color("red")
forward(80)

color("green")
forward(400)
right(90)
#making sure everthing is good


begin_fill()

color("cyan")
forward(380)
right(90)
forward(500)
right(120)
forward(205)
left(30)
forward(200)
right(90)
forward(400)
end_fill()

#second part of the sky
begin_fill()
right(90)
forward(380)
right(90)
forward(500)
right(60)

forward(200)
right(30)
forward(200)
left(90)
forward(200)
left(90)
forward(380)
left(90)
forward(400)
end_fill()


exitonclick()