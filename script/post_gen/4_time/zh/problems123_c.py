Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    ans = (n-1)//min(a, b, c, d, e) + 5
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print(5 + (n - 1) // min(a, b, c, d, e))

=======
Suggestion 3

def solve():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print(4 + (n+a-1)//a + (n+b-1)//b + (n+c-1)//c + (n+d-1)//d + (n+e-1)//e)

=======
Suggestion 4

def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    min = 0
    if a < b:
        min = a
    else:
        min = b
    if min > c:
        min = c
    if min > d:
        min = d
    if min > e:
        min = e
    if n % min == 0:
        print(n // min + 4)
    else:
        print(n // min + 5)
main()

=======
Suggestion 5

def problems123_c():
    pass

=======
Suggestion 6

def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    print(int((n-1)//min(a,b,c,d,e))+5)

=======
Suggestion 7

def solve(n,a,b,c,d,e):
    #print(n,a,b,c,d,e)
    #print(n//a,n//b,n//c,n//d,n//e)
    #print(n%a,n%b,n%c,n%d,n%e)
    if n%a == 0:
        return (n//a)*5
    elif n%a == 1:
        return (n//a)*5+1
    elif n%a == 2:
        return (n//a)*5+2
    elif n%a == 3:
        return (n//a)*5+3
    elif n%a == 4:
        return (n//a)*5+4
    elif n%a == 5:
        return (n//a)*5+5
    elif n%a == 6:
        return (n//a)*5+6
    elif n%a == 7:
        return (n//a)*5+7
    elif n%a == 8:
        return (n//a)*5+8
    elif n%a == 9:
        return (n//a)*5+9
    elif n%a == 10:
        return (n//a)*5+10
    elif n%a == 11:
        return (n//a)*5+11
    elif n%a == 12:
        return (n//a)*5+12
    elif n%a == 13:
        return (n//a)*5+13
    elif n%a == 14:
        return (n//a)*5+14
    elif n%a == 15:
        return (n//a)*5+15
    elif n%a == 16:
        return (n//a)*5+16
    elif n%a == 17:
        return (n//a)*5+17
    elif n%a == 18:
        return (n//a)*5+18
    elif n%a == 19:
        return (n//a)*5+19
    elif n%a == 20:
        return (n//a)*5+20
    elif n%a == 21:
        return (n//a)*5+21
    elif n%a == 22

=======
Suggestion 8

def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print((n-1)//min(a,b,c,d,e)+5)

=======
Suggestion 9

def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    ans = (n + min(a, b, c, d, e) - 1) // min(a, b, c, d, e) + 4
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print(5+((N-1)//min(A,B,C,D,E)))
