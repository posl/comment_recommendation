def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    #print(A,B,C,D,E)
    a = (A+9)//10*10
    b = (B+9)//10*10
    c = (C+9)//10*10
    d = (D+9)//10*10
    e = (E+9)//10*10
    #print(a,b,c,d,e)
    f = min(a,b,c,d,e)
    #print(f)
    if f == a:
        print(a+A)
    elif f == b:
        print(b+B)
    elif f == c:
        print(c+C)
    elif f == d:
        print(d+D)
    elif f == e:
        print(e+E)
