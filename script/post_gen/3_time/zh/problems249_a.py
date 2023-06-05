Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, c, d, e, f, x = map(int, input().split())
    taka = 0
    aoki = 0
    while True:
        if taka >= x:
            print("draw")
            break
        if a > 0:
            taka += b
            a -= 1
        if taka >= x:
            print("taka")
            break
        if c > 0:
            taka += 0
            c -= 1
        if taka >= x:
            print("taka")
            break
        if d > 0:
            aoki += e
            d -= 1
        if aoki >= x:
            print("aoki")
            break
        if f > 0:
            aoki += 0
            f -= 1
        if aoki >= x:
            print("aoki")
            break

=======
Suggestion 2

def run():
    a,b,c,d,e,f,x = map(int, input().split())
    taka = 0
    aoki = 0
    for i in range(10000):
        if i % (a+b+c) < a:
            taka += 1
        if i % (d+e+f) < d:
            aoki += 1
        if taka * x > aoki * x:
            print("高桥")
            return
        elif taka * x < aoki * x:
            print("青木")
            return
    print("画")

=======
Suggestion 3

def get_input():
    input_str = input()
    input_list = input_str.split(' ')
    return input_list

=======
Suggestion 4

def main():
    a, b, c, d, e, f, x = map(int, input().split())
    h = 0
    q = 0
    for i in range(x):
        if i % (a + b) < a:
            h += 1
        if i % (d + e) < d:
            q += 1
    if h > q:
        print("高桥")
    elif h < q:
        print("青木")
    else:
        print("画")

=======
Suggestion 5

def main():
    a,b,c,d,e,f,x = map(int,input().split())
    taka = 0
    aoki = 0
    for i in range(x):
        if i % (a + b) < a:
            taka += 1
        if i % (d + e) < d:
            aoki += 1
    if taka > aoki:
        print("高桥")
    elif taka < aoki:
        print("青木")
    else:
        print("画")

=======
Suggestion 6

def main():
    A,B,C,D,E,F,X = map(int,input().split())
    taka = 0
    ao = 0
    for i in range(X):
        if i % (A + B + C) < A:
            taka += 1
        if i % (D + E + F) < D:
            ao += 1
    if taka > ao:
        print("高桥")
    elif taka < ao:
        print("青木")
    else:
        print("画")

=======
Suggestion 7

def main():
    A,B,C,D,E,F,X = map(int, input().split())
    time = 0
    while X > 0:
        if A > 0:
            X -= B
            time += A
        if X <= 0:
            break
        X -= C
        if X <= 0:
            break
        if D > 0:
            X -= E
            time += D
        if X <= 0:
            break
        X -= F
    if time > 0:
        print("高桥")
    elif time < 0:
        print("青木")
    else:
        print("画")

=======
Suggestion 8

def main():
    a,b,c,d,e,f,x = map(int,input().split())
    taka = 0
    aoki = 0
    while True:
        taka += a
        if taka >= x:
            print("高桥")
            break
        aoki += d
        if aoki >= x:
            print("青木")
            break
        taka -= c
        aoki -= f
        if taka >= x and aoki >= x:
            print("画")
            break

=======
Suggestion 9

def main():
    a,b,c,d,e,f,x = map(int, input().split())
    taka = 0
    aoki = 0
    for i in range(0,x):
        if i%(a+b) < a:
            taka = taka + e
        if i%(c+d) < d:
            aoki = aoki + f
    if taka > aoki:
        print("高桥")
    elif taka < aoki:
        print("青木")
    else:
        print("画")

=======
Suggestion 10

def main():
    a,b,c,d,e,f,x = map(int, input().split())
    taka = 0
    aoki = 0
    while True:
        if taka > x and aoki > x:
            print("DRAW")
            break
        elif taka > x:
            print("AOKI")
            break
        elif aoki > x:
            print("TAKAHASHI")
            break
        else:
            taka += a
            aoki += d
            if taka > x and aoki > x:
                print("DRAW")
                break
            elif taka > x:
                print("AOKI")
                break
            elif aoki > x:
                print("TAKAHASHI")
                break
            else:
                taka += b
                aoki += e
                if taka > x and aoki > x:
                    print("DRAW")
                    break
                elif taka > x:
                    print("AOKI")
                    break
                elif aoki > x:
                    print("TAKAHASHI")
                    break
                else:
                    taka += c
                    aoki += f
