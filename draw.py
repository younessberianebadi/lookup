import turtle


f = open('FIB.txt', 'r')
fib_lines = f.read().split('\n')
for i in range(0, 20):
    pref_gotten = fib_lines[i].split('\t\t\t')[0]
    mask = pref_gotten.split('/')[1]
    address_prefix = pref_gotten.split('/')[0]
    tab = address_prefix.split(".")
    bintab = {}
    for x in range(0, 4):
        bintab[x] = bin(int(tab[x]))[2:]
    expanded_address = ''
    for x in range(0, 4):
        if len(bintab[x]) < 8:
            r = 8 - len(bintab[x])
            re = '0' * r
            bintab[x] = re + bintab[x]
            expanded_address += bintab[x]
    net_id = expanded_address[0:int(mask)]
    print('P'+str(i)+': '+net_id)
    T = turtle.Turtle()
    turtle.title('Dessin de l\'arbre binaire')
    T.speed(0)
    turtle.delay(0)
    T.reset()
    T.right(90)
    T.penup()
    T.goto(0, 250)
    T.pendown()
    branch_len = 60
    ang = 70
    for a in range(0, len(net_id)):
        if net_id[a] == '0':
            T.right(ang)
            T.forward(branch_len)
            T.write('0', align='left', font=('Arial', 6, 'normal'))
            T.left(ang)
            branch_len = branch_len - 1
        else:
            T.left(ang)
            T.forward(branch_len)
            T.write('1', align='right', font=('Arial', 6, 'normal'))
            T.right(ang)
            branch_len = branch_len - 1
    T.write('P'+str(i), align='center', font=('Arial', 10, 'bold'))
    T.penup()
    T.goto(0, 250)
    T.hideturtle()
turtle.mainloop()
