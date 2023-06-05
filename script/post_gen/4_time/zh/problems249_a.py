Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, c, d, e, f, x = map(int, input().split())
    taka = 0
    aoki = 0
    while True:
        if taka >= x:
            print('draw')
            break
        taka += a
        if taka >= x:
            print('taka')
            break
        aoki += d
        if aoki >= x:
            print('aoki')
            break
        taka += b
        aoki += e
        if taka >= x:
            print('taka')
            break
        aoki += f

=======
Suggestion 2

def main():
    A,B,C,D,E,F,X = map(int,input().split())
    taka = 0
    aoki = 0
    while True:
        if taka >= X:
            print("DRAW")
            break
        elif aoki >= X:
            print("TAKAHASHI")
            break
        taka += A
        aoki += D
        if taka >= X:
            print("TAKAHASHI")
            break
        elif aoki >= X:
            print("AOKI")
            break
        taka += B
        aoki += E
        if taka >= X:
            print("TAKAHASHI")
            break
        elif aoki >= X:
            print("AOKI")
            break
        taka += C
        aoki += F

=======
Suggestion 3

def main():
    a,b,c,d,e,f,x = map(int, input().split())
    taka = 0
    aoki = 0
    while x > 0:
        if a > x:
            taka += x
            x = 0
        else:
            taka += a
            x -= a
            if c > x:
                x = 0
            else:
                x -= c
        if d > x:
            aoki += x
            x = 0
        else:
            aoki += d
            x -= d
            if f > x:
                x = 0
            else:
                x -= f
    if taka > aoki:
        print('高桥')
    elif taka < aoki:
        print('青木')
    else:
        print('画')

=======
Suggestion 4

def main():
    a,b,c,d,e,f,x = map(int, input().split())
    taka = 0
    aoki = 0
    while True:
        if a != 0:
            taka += b
            a -= 1
        else:
            a = c
        if d != 0:
            aoki += e
            d -= 1
        else:
            d = f
        x -= 1
        if x == 0:
            if taka > aoki:
                print("高桥")
            elif taka < aoki:
                print("青木")
            else:
                print("画")
            break

=======
Suggestion 5

def main():
    a,b,c,d,e,f,x = map(int,input().split())
    taka = 0
    aoki = 0
    t = 0
    while t < x:
        if t % (a+b) < a:
            taka += 1
        if t % (d+e) < d:
            aoki += 1
        t += 1
    if taka > aoki:
        print("高桥")
    elif taka < aoki:
        print("青木")
    else:
        print("画")

=======
Suggestion 6

def run():
    a, b, c, d, e, f, x = map(int, input().split())
    t = 0
    p = 0
    while True:
        if t == x:
            print('draw')
            break
        t += 1
        if t % (a + b) <= a:
            p += d
        if t % (c + d) <= c:
            p -= e
        if p <= 0:
            print('takahashi')
            break
        if p > 0:
            print('aoki')
            break

=======
Suggestion 7

def run():
    A, B, C, D, E, F, X = map(int, input().split())
    taka = 0
    aoki = 0
    for i in range(X):
        if i % (A+B) < A:
            taka += 1
        if i % (D+E) < D:
            aoki += 1
    if taka > aoki:
        print("高桥")
    elif taka < aoki:
        print("青木")
    else:
        print("画")

run()

=======
Suggestion 8

def main():
    a,b,c,d,e,f,x = map(int, input().split())
    taka = 0
    aoki = 0
    while x > 0:
        if a > 0:
            taka += b
            a -= 1
        else:
            a += c
        if d > 0:
            aoki += e
            d -= 1
        else:
            d += f
        x -= 1
    if taka > aoki:
        print("高桥")
    elif taka < aoki:
        print("青木")
    else:
        print("画")

=======
Suggestion 9

def main():
    #读取数据
    a,b,c,d,e,f,x = map(int,input().split())
    #计算高桥和青木的行走距离
    tq = 0
    tq += (a+b)*c
    tq += a*(x//(a+b))
    tq += min(a,x%(a+b))
    ta = 0
    ta += (d+e)*f
    ta += d*(x//(d+e))
    ta += min(d,x%(d+e))
    #比较
    if tq > ta:
        print("高桥")
    elif tq < ta:
        print("青木")
    else:
        print("画")

=======
Suggestion 10

def main():
    a,b,c,d,e,f,x = map(int,input().split())
    taka = 0
    aoki = 0
    while True:
        if taka >= x and aoki >= x:
            print('DRAW')
            break
        taka += a
        aoki += d
        if taka >= x and aoki >= x:
            print('DRAW')
            break
        aoki += e
        if taka >= x and aoki >= x:
            print('DRAW')
            break
        taka += b
        if taka >= x and aoki >= x:
            print('DRAW')
            break
        if taka > aoki:
            print('TAKAHASHI')
            break
        elif taka < aoki:
            print('AOKI')
            break
