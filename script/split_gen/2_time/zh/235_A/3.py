def problem235_a():
    abc = input()
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    result = a*100+b*10+c + b*100+c*10+a + c*100+a*10+b
    print(result)
