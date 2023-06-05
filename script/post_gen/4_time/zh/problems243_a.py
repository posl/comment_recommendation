Synthesizing 10/10 solutions

=======
Suggestion 1

def problems243_a():
    v,a,b,c = map(int,input().split())
    if v % a == 0 or v % b == 0 or v % c == 0:
        print('T')
    else:
        print('F')

=======
Suggestion 2

def problems243_a():
    v, a, b, c = map(int, input().split())
    sum = 0
    while True:
        sum += 1
        if v < a:
            print('F')
            break
        v -= a
        if v < b:
            print('M')
            break
        v -= b
        if v < c:
            print('T')
            break
        v -= c

problems243_a()

=======
Suggestion 3

def washhairs(v,a,b,c):
    if v < a:
        return 'F'
    elif v < a+b:
        return 'M'
    else:
        return 'T'

=======
Suggestion 4

def main():
    # 读取输入
    v, a, b, c = map(int, input().split())
    # 依次计算
    while v > 0:
        if v >= a:
            v -= a
        else:
            print('F')
            return
        if v >= b:
            v -= b
        else:
            print('M')
            return
        if v >= c:
            v -= c
        else:
            print('T')
            return

=======
Suggestion 5

def main():
    v,a,b,c = map(int, input().split())
    while v >= 0:
        v -= a
        if v < 0:
            print("F")
            break
        v -= b
        if v < 0:
            print("M")
            break
        v -= c
        if v < 0:
            print("T")
            break

=======
Suggestion 6

def problems243_a():
    v,a,b,c = map(int, input().split())
    while v >= 0:
        v -= a
        if v < 0:
            print("F")
            break
        v -= b
        if v < 0:
            print("M")
            break
        v -= c
        if v < 0:
            print("T")
            break
    return 0

=======
Suggestion 7

def solve():
    v, a, b, c = map(int, input().split())
    while v > 0:
        v -= a
        if v < 0:
            print('F')
            break
        v -= b
        if v < 0:
            print('M')
            break
        v -= c
        if v < 0:
            print('T')
            break

solve()

=======
Suggestion 8

def main():
    v, a, b, c = map(int, input().split())
    while v:
        if v < a:
            print('F')
            break
        elif v < b:
            print('M')
            break
        elif v < c:
            print('T')
            break
        else:
            v -= a
            v -= b
            v -= c

=======
Suggestion 9

def main():
    # 读取输入
    v, a, b, c = map(int, input().split())

    # 模拟
    while True:
        # 高桥的父亲
        v -= a
        if v < 0:
            print('F')
            break

        # 高桥的母亲
        v -= b
        if v < 0:
            print('M')
            break

        # 高桥
        v -= c
        if v < 0:
            print('T')
            break

=======
Suggestion 10

def main():
    v,a,b,c = map(int,input().split())
    while v >= 0:
        if v >= a:
            v -= a
            if v >= b:
                v -= b
                if v >= c:
                    v -= c
                    if v >= 0:
                        continue
                    else:
                        print('T')
                        break
                else:
                    print('C')
                    break
            else:
                print('B')
                break
        else:
            print('A')
            break
