import calculator

controlKey = 1

while controlKey != 4:
    print "This is your CALCULADORA"
    print "Insert n1: "
    n1 = input()
    print "Insert n2: "
    n2 = input()

    c = calculator.Calculator()
    c.setData(n1,n2)

    print "#1: add"
    print "#2: sub"
    print "#3: div"
    print "#4: exit"
    controlKey = input()
    if controlKey is 1:
        print c.add()
    elif controlKey is 2:
        print c.subtract()
    elif controlKey is 3:
        print c.divide()


