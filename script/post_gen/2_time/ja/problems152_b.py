Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if str(a) * b < str(b) * a:
        print(str(a) * b)
    else:
        print(str(b) * a)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    x = str(a) * b
    y = str(b) * a
    if x < y:
        print(x)
    else:
        print(y)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    aa = str(a) * b
    bb = str(b) * a
    if aa < bb:
        print(aa)
    else:
        print(bb)

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if a * b > 0:
        if str(a) * b < str(b) * a:
            print(str(a) * b)
        else:
            print(str(b) * a)

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    if a * b == 0:
        print(0)
    elif a >= b:
        print(str(a) * b)
    else:
        print(str(b) * a)

=======
Suggestion 6

def main():
    a,b = map(int,input().split())
    if a*b == 0:
        print(0)
        return
    if a < b:
        print(str(a)*b)
    else:
        print(str(b)*a)

main()

=======
Suggestion 7

def   main (): 
     a , b  =  map ( int ,  input (). split ()) 
     print ( min ( str ( a ) * b ,  str ( b ) * a ))

=======
Suggestion 8

def main():
    a,b = map(int,input().split())
    if a*b == 0:
        print(0)
    else:
        print(str(a)*b if a<b else str(b)*a)

=======
Suggestion 9

def main():
    a,b = map(int,input().split())
    if a*b == 0:
        print("0")
    elif a*b < 10:
        print(str(a)*b)
    else:
        print(str(b)*a)
