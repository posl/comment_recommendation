Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    res = 0
    if a % 10 != 0:
        res = max(res, a + 10 - a % 10)
    else:
        res = max(res, a)
    if b % 10 != 0:
        res = max(res, b + 10 - b % 10)
    else:
        res = max(res, b)
    if c % 10 != 0:
        res = max(res, c + 10 - c % 10)
    else:
        res = max(res, c)
    if d % 10 != 0:
        res = max(res, d + 10 - d % 10)
    else:
        res = max(res, d)
    if e % 10 != 0:
        res = max(res, e + 10 - e % 10)
    else:
        res = max(res, e)
    print(res)

=======
Suggestion 2

def main():
    dishes = []
    for i in range(5):
        dishes.append(int(input()))
    min_time = 100000000000
    for i in range(5):
        if dishes[i] < min_time:
            min_time = dishes[i]
    for i in range(5):
        if dishes[i] % 10 != 0:
            dishes[i] = dishes[i] + 10 - dishes[i] % 10
    print(dishes[0] + dishes[1] + dishes[2] + dishes[3] + dishes[4])

=======
Suggestion 3

def solution(a,b,c,d,e):
    res = 0
    if a%10 > 0:
        res = a + (10 - a%10)
    else:
        res = a
    if b%10 > 0:
        res = min(res, b + (10 - b%10))
    else:
        res = min(res, b)
    if c%10 > 0:
        res = min(res, c + (10 - c%10))
    else:
        res = min(res, c)
    if d%10 > 0:
        res = min(res, d + (10 - d%10))
    else:
        res = min(res, d)
    if e%10 > 0:
        res = min(res, e + (10 - e%10))
    else:
        res = min(res, e)
    return res

=======
Suggestion 4

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    min_time = min(a%10,b%10,c%10,d%10,e%10)
    if min_time == 0:
        min_time = 10
    print(str((a//10+1)*10)+str((b//10+1)*10)+str((c//10+1)*10)+str((d//10+1)*10)+str((e//10+1)*10))
    #print((a//10+1)*10)

=======
Suggestion 5

def solution():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    if A % 10 == 0:
        pass
    else:
        A = (A // 10 + 1) * 10
    if B % 10 == 0:
        pass
    else:
        B = (B // 10 + 1) * 10
    if C % 10 == 0:
        pass
    else:
        C = (C // 10 + 1) * 10
    if D % 10 == 0:
        pass
    else:
        D = (D // 10 + 1) * 10
    if E % 10 == 0:
        pass
    else:
        E = (E // 10 + 1) * 10
    return A + B + C + D + E

=======
Suggestion 6

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    #print(a,b,c,d,e)
    #print(type(a),type(b),type(c),type(d),type(e))

    #print(a%10,b%10,c%10,d%10,e%10)
    #print(type(a%10),type(b%10),type(c%10),type(d%10),type(e%10))

    #print(a//10,b//10,c//10,d//10,e//10)
    #print(type(a//10),type(b//10),type(c//10),type(d//10),type(e//10))

    #print(a//10*10,b//10*10,c//10*10,d//10*10,e//10*10)
    #print(type(a//10*10),type(b//10*10),type(c//10*10),type(d//10*10),type(e//10*10))

    #print(a//10*10+10,b//10*10+10,c//10*10+10,d//10*10+10,e//10*10+10)
    #print(type(a//10*10+10),type(b//10*10+10),type(c//10*10+10),type(d//10*10+10),type(e//10*10+10))

    #print(a//10*10+10-a,b//10*10+10-b,c//10*10+10-c,d//10*10+10-d,e//10*10+10-e)
    #print(type(a//10*10+10-a),type(b//10*10+10-b),type(c//10*10+10-c),type(d//10*10+10-d),type(e//10*10+10-e))

    #print(a//10*10+10-a+b//10*10+10-b+c//10*10+10-c+d//10*10+10-d+e//10*10+10-e)
    #print(type(a//10*10+10-a+b//10*10+10-b+c//10*10+10-c+d//10*10+10-d+e//10*10+10-e))

    #print(a//

=======
Suggestion 7

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print(min(a%10 and 10-a%10 or 0, b%10 and 10-b%10 or 0, c%10 and 10-c%10 or 0, d%10 and 10-d%10 or 0, e%10 and 10-e%10 or 0) + a + b + c + d + e)

=======
Suggestion 8

def readinput():
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    e=int(input())
    return a,b,c,d,e

=======
Suggestion 9

def problems123_b():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    if a%10 == 0:
        a1 = a
    else:
        a1 = (a//10+1)*10
    if b%10 == 0:
        b1 = b
    else:
        b1 = (b//10+1)*10
    if c%10 == 0:
        c1 = c
    else:
        c1 = (c//10+1)*10
    if d%10 == 0:
        d1 = d
    else:
        d1 = (d//10+1)*10
    if e%10 == 0:
        e1 = e
    else:
        e1 = (e//10+1)*10
    print(a1+b1+c1+d1+e1)
problems123_b()

=======
Suggestion 10

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    a = A % 10
    b = B % 10
    c = C % 10
    d = D % 10
    e = E % 10
    if a == 0:
        a = 10
    if b == 0:
        b = 10
    if c == 0:
        c = 10
    if d == 0:
        d = 10
    if e == 0:
        e = 10
    if A % 10 == 0:
        A = A - 10
    else:
        A = A - A % 10
    if B % 10 == 0:
        B = B - 10
    else:
        B = B - B % 10
    if C % 10 == 0:
        C = C - 10
    else:
        C = C - C % 10
    if D % 10 == 0:
        D = D - 10
    else:
        D = D - D % 10
    if E % 10 == 0:
        E = E - 10
    else:
        E = E - E % 10
    if a + b + c + d + e == 10:
        print(A + B + C + D + E + 10)
    else:
        print(A + B + C + D + E)
