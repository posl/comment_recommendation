Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a == b:
        print("IMPOSIBLE")
    else:
        print(int((a+b)/2))

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if (a + b) % 2 != 0:
        print("IMPOSSIBLE")
    else:
        print((a + b) // 2)

=======
Suggestion 3

def solve(a,b):
    if a == b:
        return a
    elif a > b:
        if (a - b) % 2 == 0:
            return (a - b) // 2
        else:
            return "IMPOSSIBLE"
    else:
        if (b - a) % 2 == 0:
            return (b - a) // 2
        else:
            return "IMPOSSIBLE"

=======
Suggestion 4

def main():
    a,b = map(int, input().split())
    if (a+b)%2 == 0:
        print(int((a+b)/2))
    else:
        print("IMPOSSIBLE")

=======
Suggestion 5

def main():
    # 读取输入
    a, b = map(int, input().split())

    # 处理
    if (a + b) % 2 == 0:
        print((a + b) // 2)
    else:
        print("IMPOSSIBLE")

=======
Suggestion 6

def problems135_a():
    a,b=map(int,input().split())
    if (a+b)%2==0:
        print((a+b)//2)
    else:
        print('IMPOSIBLE')

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    if (a + b) % 2 == 0:
        print((a + b) // 2)
    else:
        print('IMPOSSIBLE')

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    if (a + b) % 2 == 0:
        print(int((a + b) / 2))
    else:
        print('IMPOSSIBLE')
