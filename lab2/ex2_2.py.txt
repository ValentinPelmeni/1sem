import turtle as t
def a_1():
    t.pendown()
    t.forward(50)
    t.backward(50)
    t.penup()
def a_2():
    t.penup()
    t.left(90)
    t.forward(50)
    t.right(90)
    a_1()
    t.right(90)
    t.forward(50)
    t.left(90)
def a_3():
    t.penup()
    t.left(90)
    t.forward(100)
    t.right(90)
    a_1()
    t.right(90)
    t.forward(100)
    t.left(90)
def a_4_1():
    t.pendown()
    t.left(90)
    t.forward(50)
    t.penup()
    t.forward(50)
    t.backward(100)
    t.right(90)
    t.penup()
def a_4_2():
    t.pendown()
    t.left(90)
    t.penup()
    t.forward(50)
    t.pendown()
    t.forward(50)
    t.penup()
    t.backward(100)
    t.right(90)
    t.penup()
def a_5_1():
    t.penup()
    t.forward(50)
    a_4_1()
    t.backward(50)
def a_5_2():
    t.penup()
    t.forward(50)
    a_4_2()
    t.backward(50)
def a_6():
    t.pendown()
    t.left(45)
    t.forward((2*(50**2))**0.5)
    t.left(225)
    t.penup()
    t.forward(50)
    t.left(90)
    t.backward(50)
    t.penup()
def a_7():
    t.penup()
    t.left(90)
    t.forward(50)
    t.left(270)
    a_6()
    t.right(90)
    t.forward(50)
    t.left(90)
def a_0():
    t.penup
    t.forward(70)
def b0():
    a_1()
    a_3()
    a_4_1()
    a_4_2()
    a_5_1()
    a_5_2()
    a_0()
def b1():
    a_7()
    a_5_1()
    a_5_2()
    a_0()
def b2():
    a_3()
    a_5_2()
    a_2()
    a_4_1()
    a_1()
    a_0()
def b3():
    a_3()
    a_2()
    a_1()
    a_5_1()
    a_5_2()
    a_0()
def b4():
    a_2()
    a_4_2()
    a_5_1()
    a_5_2()
    a_0()
def b5():
    a_3()
    a_1()
    a_2()
    a_4_2()
    a_5_1()
    a_0()
def b6():
    a_3()
    a_2()
    a_1()
    a_4_1()
    a_4_2()
    a_5_1()
    a_0()
def b7():
    a_3()
    a_7()
    a_4_1()
    a_0()
def b8():
    a_1()
    a_2()
    a_3()
    a_4_1()
    a_4_2()
    a_5_1()
    a_5_2()
    a_0()
def b9():
    a_1()
    a_2()
    a_3()
    a_4_2()
    a_5_1()
    a_5_2()
    a_0()
def _pochta():
    y= input()
    for i in range(len(y)):
        if y[i] == "1":
            b1()
        elif y[i] == "0":
            b0()
        elif y[i] == "2":
            b2()
        elif y[i] == "3":
            b3()
        elif y[i] == "4":
            b4()
        elif y[i] == "5":
            b5()
        elif y[i] == "6":
            b6()
        elif y[i] == "7":
            b7()
        elif y[i] == "8":
            b8()
        else:
            b9()
_pochta()
    
    


    
    