from tkinter import*
from random import*
from tkinter import ttk
otvet='*Скуф сидит на стуле и играет в танки'
mat=0 #матевация
skip=0
day=1 #дни
pr=2 #правильный ответ
nash=0 #наш ответ(игрока)
kr=0

def m1(): #в случае нажетия 1 кнопки
    global nash
    nash=1
    week()

def m2(): #в случае нажетия 2 кнопки
    global nash
    nash=2
    week()

def m3(): #в случае нажетия 3 кнопки
    global nash
    nash=3
    week()

def week(): #ниделя
    global mat, day, pr, nash, otvet, kr







#все, что связанно с диалогами (там был ещё один "0" диалог, он не тут
    if day == 1:        #1 диалог
        pr=2
        otvet='Мне прекрастно живется'
        b1["text"]='Ты прав, мне тоже'
        b2["text"]='Тебе нравится быть свиньей?'
        b3["text"]='Может спортом займешься?'
    elif day == 2: #2 диалог
        pr=3
        otvet='Хотя может спортом занятся?'
        b1["text"]='Киберспортом'
        b2["text"]='С понедельника'
        b3["text"]='Это правильно'
    elif day==3: # поход в зал

        nash=skip
        if mat>5:
            otvet='Скуф отправился в качалку'
            b1["text"]='КРУТО!'
            b2["text"]='КАЙФ!'
            b3["text"]='МОЛОДЕЦ!'
            root.image = PhotoImage(file='2.png')
            bg_logo['image']=root.image
            mat=0
            kr=kr+1
        else:
            otvet='Скуф просто лежит на диване'
            b1["text"]='ЛОХ!'
            b2["text"]='БАЛБЕС!'
            b3["text"]='ДУРАК!'
            mat=0


    elif day == 4: #3 диалог
        pr=3
        otvet='*Скуф снова играет в танки'
        b1["text"]='Ты забил на зал?'
        b2["text"]='ИДИ РАБОТАЙ'
        b3["text"]='Ну и заплывай жиром'
        root.image = PhotoImage(file='skyf.png')
        bg_logo['image']=root.image


    elif day == 5: #4 диалог
        pr=1
        otvet='Я очень устал'
        b1["text"]='Не оправдывайся'
        b2["text"]='Ты можешь!'
        b3["text"]='Ты всегда такой'

    elif day == 6: #5 диалог
        pr=2
        otvet='Наверное я могу пойти в зал'
        b1["text"]='Не умрешь'
        b2["text"]='Сначала есть'
        b3["text"]='Наверное'
    elif day==7: # поход в зал


        if mat>5:
            otvet='Скуф отправился в качалку'
            b1["text"]='КРУТО!'
            b2["text"]='КАЙФ!'
            b3["text"]='МОЛОДЕЦ!'
            root.image = PhotoImage(file='2.png')
            bg_logo['image']=root.image
            mat=0
            kr=kr+1
        else:
            otvet='Скуф просто лежит на диване'
            b1["text"]='ЛОХ!'
            b2["text"]='БАЛБЕС!'
            b3["text"]='ДУРАК!'
            mat=0


    elif day == 8: #6 диалог
        pr=1
        otvet='*Скуф лежит на кровати с тревожным видом'
        b1["text"]='В ЗАЛ!'
        b2["text"]='Пошли в танки'
        b3["text"]='Нужно в магазин сходить'
        root.image = PhotoImage(file='skyf.png')
        bg_logo['image']=root.image
    elif day == 9: #7 диалог
        pr=1
        otvet='Ты не видишь? Я сплю!'
        b1["text"]='Уже нет'
        b2["text"]='Это что-то меняет?'
        b3["text"]='Потом выспишься'
    elif day == 10: #8 диалог
        otvet='Ты уверен, что это нужно?'
        b1["text"]='ДА'
        b2["text"]='Ладно, иди спи'
        b3["text"]='А ты?'
        pr=3
    elif day==11: # поход в зал


        nash=skip
        if mat>5:
            otvet='Скуф отправился в качалку'
            b1["text"]='КРУТО!'
            b2["text"]='КАЙФ!'
            b3["text"]='МОЛОДЕЦ!'
            root.image = PhotoImage(file='2.png')
            bg_logo['image']=root.image
            mat=0
            kr=kr+1
        else:
            otvet='Скуф просто лежит на диване'
            b1["text"]='ЛОХ!'
            b2["text"]='БАЛБЕС!'
            b3["text"]='ДУРАК!'
            mat=0

    elif day == 12: #9 диалог
        otvet='Скуф смотрит фильм'
        b1["text"]='Напоминать стоит?'
        b2["text"]='Фильм отстой'
        b3["text"]='ЖРАТЬ'
        root.image = PhotoImage(file='skyf.png')
        bg_logo['image']=root.image
        pr=1
    elif day == 13: #10 диалог
        pr=1
        otvet='Тебе не надоело?'
        b1["text"]='нет'
        b2["text"]='ДА'
        b3["text"]='Не надоело сидеть?'
    elif day == 14: #11 диалог
        pr=3
        otvet='Может ты прав'
        b1["text"]='уже поздно'
        b2["text"]='Никогда не поздно'
        b3["text"]='Я в шутку продолжаю'
    elif day == 15: #тут в будушем концовка(А пока поход в зал)
        nash=skip
        if mat>5:
            otvet='Скуф отправился в качалку'
            b1["text"]='КРУТО!'
            b2["text"]='КАЙФ!'
            b3["text"]='МОЛОДЕЦ!'
            root.image = PhotoImage(file='2.png')
            bg_logo['image']=root.image
            mat=0
            kr=kr+1
        else:
            otvet='Скуф просто лежит на диване'
            b1["text"]='ЛОХ!'
            b2["text"]='БАЛБЕС!'
            b3["text"]='ДУРАК!'
            mat=0
        if kr>=3:
            otvet='Скуф теперь ГИГАЧАД'
            b1["text"]='ТЫ'
            b2["text"]='ТОЖЕ'
            b3["text"]='МОЖЕШЬ!'
            root.image = PhotoImage(file='3.png')
            bg_logo['image']=root.image
        if kr<3:
            otvet='Скуф ничего не смог изметь...(Не будь как Скуф)'
            b1["text"]='БУДЬ'
            b2["text"]='ЛУЧШЕ'
            b3["text"]='СКУФА!'
            root.image = PhotoImage(file='1.png')
            bg_logo['image']=root.image




    if nash==pr:       #+ и - матевация за ответы
        mat=mat+3
    elif nash==skip: #это скип для похода в зал и ничего неделание
        mat=mat+0
    else:
        mat=mat-2

    day =day+1   #счетчик дней









    l["text"]=otvet


    if mat<0:
        mat=0      #чтобы матевация не уходила ниже нуля

    l1["value"]=mat  #счетчик матевации


root = Tk()









root.geometry('1200x628') #размер окна
root.resizable(width=False , height=False)

root.image = PhotoImage(file="skyf.png")
bg_logo = Label(root, image=root.image)
bg_logo.place(anchor='nw')


l1=ttk.Progressbar(orient="vertical", length=100, value=mat, maximum=9) #шкала матевации
l1.place(x=1170,width=20,y=200, height=200)

l=Label(root,bg="lightblue",width="50",font="Arial 16", text='*Скуф сидит на стуле и играет в танки') #шкала дней(она в будушем заменится на диалоговое окно, и игрок не будет считать дни)
l.place(x=268,width=562,y=500)

b1 = Button (root, text='Пошли выпьем!', bg = 'yellow', command= m1) #кнопка 1
b1.place(x=268,width=165,y=550)


b2 = Button (root, text='Тебе не надоело так жить?', bg = 'yellow', command= m2) #кнопка 2
b2.place(x=460,width=170,y=550)



b3 = Button (root, text='Ты спать  не хочешь?', bg = 'yellow', command= m3) #кнопка 3
b3.place(x=665,width=165,y=550)








root.mainloop()