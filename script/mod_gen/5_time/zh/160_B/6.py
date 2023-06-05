def problem160_b():
    a = int(input())
    b = a//500
    c = a%500
    d = c//5
    e = c%5
    print(1000*b+5*d)
problem160_b()
