Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y = map(int, input().split())
    for i in range(x+1):
        j = x - i
        if 2*i + 4*j == y:
            print("Yes")
            return
    print("No")

=======
Suggestion 2

def main():
    x, y = map(int, input().split())
    for i in range(x + 1):
        if i * 4 + (x - i) * 2 == y:
            print('Yes')
            exit()
    print('No')

=======
Suggestion 3

def check(X,Y):
    # 鶴の数をt, 亀の数をkとすると
    # t + k = X
    # 2 * t + 4 * k = Y
    # これを解くと
    # t = Y / 2 - X
    # k = 2 * X - Y / 2
    # である。
    # これが整数であることを確認すればよい。
    t = Y / 2 - X
    k = 2 * X - Y / 2
    if t >= 0 and k >= 0 and t == int(t) and k == int(k):
        return True
    else:
        return False

=======
Suggestion 4

def check():
    x,y = map(int,input().split())
    if x == 1 or x == 2:
        if y == 2 or y == 4:
            print("Yes")
        else:
            print("No")
    else:
        if y == 2*x or y == 4*x:
            print("Yes")
        else:
            print("No")

=======
Suggestion 5

def solve():
    x, y = map(int, input().split())
    for i in range(x+1):
        if i*2 + (x-i)*4 == y:
            print('Yes')
            return
    print('No')

=======
Suggestion 6

def main():
    x, y = map(int, input().split())
    if y % 2 == 0 and (y - x * 2) % 2 == 0 and (y - x * 2) / 2 >= 0 and x - (y - x * 2) / 2 >= 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    x, y = map(int, input().split())
    for i in range(x+1):
        j = x - i
        if i*2 + j*4 == y:
            print('Yes')
            return
    print('No')

=======
Suggestion 8

def solve():
    x, y = map(int, input().split())
    for i in range(x+1):
        if 2*i + 4*(x-i) == y:
            return "Yes"
    return "No"

=======
Suggestion 9

def main():
    x, y = map(int, input().split())
    for i in range(x+1):
        if i * 4 + (x-i) * 2 == y:
            print('Yes')
            return
    print('No')

=======
Suggestion 10

def main():
    x,y = map(int, input().split())

    if y % 2 == 0 and y >= 2 * x and y <= 4 * x:
        print('Yes')
    else:
        print('No')
