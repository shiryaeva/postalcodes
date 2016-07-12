#! /usr/bin/python3
#-*- coding: utf-8 -*

def main():
    s = input('Ведите число x: ')
    if s.isdigit():
        draw_numbers(s)
    else:
        print('Ввод содержит нецифровой символ')

"""
    t=turtle.Turtle()
    t.shape("turtle")
    t.color("green")
    t.shapesize(1)
    t.penup()
    t.pensize(10)
    t.backward(450)
    draw_number(t,x)
"""

def digit0(t,l1,l2):
    """Рисует нолик, возвращает черепашку в исходную точку"""
    B=[90,90,90,90]
    A=[l2,l1,l2,l1]
    t.pendown()
    graf(t,A,B)
    t.penup()
    t.forward(l2+l2/2)

def digit1(t,l1,l2,l3):
    """Рисует один, возвращает черепашку в исходную точку"""
    t.forward(l2)
    t.left(90)
    t.pendown()
    t.forward(l1)
    t.left(135)
    t.forward(l3)
    t.penup()
    t.left(90)
    t.forward(l3)
    t.left(45)
    t.forward(l2/2)

def digit2(t,l1,l2,l3):
    """Рисует два, возвращает черепашку в исходную точку"""
    t.forward(l2)
    t.left(180)
    A=[l2,l3,l2,l2]
    B=[-135,45,90,90]
    graf(t,A,B)
    back(t,l1,90)
    t.forward(l2+l2/2)

def digit3(t,l1,l2,l3):
    """Рисует три, возвращает черепашку в исходную точку"""
    t.left(45)
    A=[l3,l2,l3,l2]
    B=[135,-135,135,90]
    graf(t,A,B)
    back(t,l1,90)
    t.forward(l2+l2/2)

def digit4(t,l1,l2):
    """Рисует четыре, возвращает черепашку в исходную точку"""
    t.forward(l2)
    t.left(90)
    A=[l1,l2,l2,l2]
    B=[180,-90,-90,180]
    graf(t,A,B)
    back(t,l1,90)
    t.forward(l2+l2/2)

def digit5(t,l1,l2):
    """Рисует пять, возвращает черепашку в исходную точку"""
    A=[l2,l2,l2,l2,l2]
    B=[90,90,-90,-90,-90]
    graf(t,A,B)
    back(t,l1,90)
    t.forward(l2/2)

def digit6(t,l1,l2,l3):
    """Рисует шесть, возвращает черепашку в исходную точку"""
    t.left(90)
    t.forward(l2)
    t.left(-90)
    A=[l2,l2,l2,l2,l3]
    B=[-90,-90,-90,-45,-135]
    graf(t,A,B)
    back(t,l1,90)
    t.forward(l2/2)

def digit7(t,l1,l2,l3):
    """Рисует семь, возвращает черепашку в исходную точку"""
    t.left(90)
    A=[l2,l3,l2]
    B=[-45,135,90]
    graf(t,A,B)
    back(t,l1,90)
    t.forward(l2+l2/2) 

def digit8(t,l1,l2):
    """Рисует восемь, возвращает черепашку в исходную точку"""
    A=[l2,l1,l2,l1,l2,l2]
    B=[90,90,90,180,-90,-90]
    graf(t,A,B)
    back(t,l2,90)
    t.forward(l2/2)

def digit9(t,l2,l3):
    """Рисует девять, возвращает черепашку в исходную точку"""
    t.left(45)
    A=[l3,l2,l2,l2,l2]
    B=[45,90,90,90,-90]
    graf(t,A,B)
    back(t,l2,90)
    t.forward(l2/2) 

def back(t,st,gr):
    """Взврат черепушки""" 
    t.penup()
    t.forward(st)
    t.left(gr)

def graf(t,A,B):
    """Рисование цифры"""
    t.pendown()
    for length, degree in zip(A,B):
        t.forward(length)
        t.left(degree)

def draw_numbers(x):
    """
        Рисует черепашкой цифры числа x в 10-ой СС
        Окно появляется только если ввод корректный
    """
    N = len(x)
    L = 160
    l1 = L
    l2 = 0.5*L
    l3 = 2**0.5 * l2
    import turtle
    # Подгоняем размеры окна для рисования
    turtle.setup((0.75*N+0.5)*L, 2*L)
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    t.setpos((0.125-N*0.375)*L,-L*0.5)
    t.color("green")
    t.pensize(16)
    for i in range(N):
        a=x[i]
        if a=='0':
            digit0(t,l1,l2)
        elif a=='1':
            digit1(t,l1,l2,l3)
        elif a=='2':
            digit2(t,l1,l2,l3)
        elif a=='3':
            digit3(t,l1,l2,l3)
        elif a=='4':
            digit4(t,l1,l2)
        elif a=='5':
            digit5(t,l1,l2)
        elif a=='6':
            digit6(t,l1,l2,l3)
        elif a=='7':
            digit7(t,l1,l2,l3)
        elif a=='8':
            digit8(t,l1,l2)
        elif a=='9':
            digit9(t,l2,l3)
        else:
            print('Ввели не число')
    # Остаёмся ждать закрытия окна черепашки
    turtle.done()


main()
