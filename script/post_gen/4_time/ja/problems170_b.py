Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y = map(int, input().split())
    if y % 2 == 0 and y >= 2 * x and y <= 4 * x:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    x, y = map(int, input().split())
    for i in range(x + 1):
        if i * 2 + (x - i) * 4 == y:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 3

def main():
    X, Y = map(int, input().split())
    for i in range(X+1):
        if i*4 + (X-i)*2 == Y:
            print('Yes')
            return
    print('No')

=======
Suggestion 4

def solve():
    x, y = map(int, input().split())
    for i in range(x+1):
        if i*4 + (x-i)*2 == y:
            return "Yes"
    return "No"

print(solve())

=======
Suggestion 5

def solve():
    x,y = map(int,input().split())
    for i in range(x+1):
        j = x-i
        if 2*i+4*j == y:
            print("Yes")
            return
    print("No")

=======
Suggestion 6

def solve():
    X, Y = map(int, input().split())
    for i in range(X+1):
        if i*4 + (X-i)*2 == Y:
            return 'Yes'
    return 'No'

print(solve())

=======
Suggestion 7

def main():
    X, Y = map(int, input().split())
    if Y % 2 == 0:
        if 2 * X <= Y and 4 * X >= Y:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

=======
Suggestion 8

def main():
    x,y = map(int,input().split())
    if (y % 2 == 0) and (y >= 2*x) and (y <= 4*x):
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def check(x,y):
    if x*2 <= y and y <= x*4 and y%2 == 0:
        return True
    else:
        return False

x,y = map(int,input().split())

=======
Suggestion 10

def main():
    x, y = map(int, input().split())
    # 鶴の数を i として全探索
    for i in range(x+1):
        # 鶴の数が決まれば亀の数も決まる
        j = x - i
        if 2*i + 4*j == y:
            print("Yes")
            return
    print("No")
