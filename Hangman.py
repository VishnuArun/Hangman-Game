#draw hangman
import turtle
import random
turtle.hideturtle()
turtle.speed(0)
def turtleinitial(): #This should set up the gallow and lines# return word
    turtle.goto(0,0)
    word = wordlist()
    length = len(word)
    x = 0
    turtle.penup()
    while x<length:
        turtle.write("_",font="10")
        turtle.forward(25)
        x+=1
    turtle.goto(0,0)
    turtle.penup
    turtle.left(90)
    turtle.forward(35)
    turtle.pendown()
    turtle.forward(350)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(20)
    return word

def wordprint(indexlist,letter):
    list1 = indexlist
    value = letter
    turtle.penup()
    turtle.setheading(0)
    
    for x in list1:
        turtle.goto(0,0)
        turtle.forward(25*x)
        turtle.pendown
        turtle.write(str.upper(letter),font="10")
    
def hangman(x):# have this function return pen to origin so the text is easy 
    count = x
    
    if count == 1:
        turtle.penup()
        turtle.setheading(270)
        turtle.goto(200,365)
        turtle.forward(100)
        turtle.left(90)
        turtle.pendown()
        turtle.circle(50)
        turtle.penup()
           
    elif count == 2:
        turtle.penup()
        turtle.goto(200,165)
        turtle.setheading(270)
        turtle.backward(100)
        turtle.pendown()
        turtle.forward(150)
        turtle.penup()
        
    elif count == 3:
        turtle.penup()
        turtle.goto(200,165)
        turtle.setheading(270)
        turtle.backward(30)
        turtle.pendown()
        turtle.left(135)
        turtle.forward(70)
        turtle.penup()

    elif count == 4:
        turtle.penup()
        turtle.setheading(270)
        turtle.goto(200,165)
        turtle.backward(30)
        turtle.pendown()
        turtle.right(135)
        turtle.forward(70)
        turtle.penup()

    elif count == 5:
        turtle.penup()
        turtle.setheading(270)
        turtle.goto(200,215)
        turtle.forward(100)
        turtle.pendown()
        turtle.left(45)
        turtle.forward(70)
        turtle.penup()

    elif count == 6:
        turtle.penup()
        turtle.setheading(270)
        turtle.goto(200,215)
        turtle.forward(100)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(70)
        turtle.penup()
        turtle.setheading(270)
        turtle.goto(-40,-60)
        turtle.write("Sorry, you lose!",font="40")#You lose

#return random word
def wordlist():
    list1 = ['banana','orange','pineapple','mango','strawberry','peach','guava','grape','tangerine','cantelope','blackberry','blueberry','watermelon','apple','pear','kiwi','tomato','lime','lemons','coconut']
    z = random.randint(0,len(list1)-1)
    word = list1[z]
    return word
#return letter
def inputv():
    letter = str(turtle.textinput("Guess a letter","Enter a single letter here: "))
    if len(letter) == 1:
        return(str.lower(letter))
    else:
        return inputv()

#this function returns only index
def indexfind(word,letter):
     
    x=0
    y=[]
    while x < len(word):
        if word[x] == letter:
            y.append(x)
            x+=1
        
        else:
            x+=1
    return (y)
#starter function
def main():
    word = turtleinitial()
    terminate = word
    count = 1
    while count < 7 and len(terminate) > 0:
        letter =inputv()
        y = indexfind(word,letter)
        if len(y) == 0:
            hangman(count)
            count+=1
        else:
            wordprint(y,letter)
            word = word.replace(letter,' ')
            terminate = terminate.replace(letter,'')
    if len(terminate)==0:
        turtle.goto(-40,-60)
        turtle.setheading(270)
        turtle.write("Congratulations!!",font="40")#You win
main()