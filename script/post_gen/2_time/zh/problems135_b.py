Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(a, b):
    if (a+b)%2==0:
        return (a+b)//2
    else:
        return "IMPOSSIBLE"

a, b = map(int, input().split())
print(solve(a, b))

=======
Suggestion 2

def main():
    a,b = map(int,input().split())
    if (a+b)%2 == 0:
        print((a+b)//2)
    else:
        print("IMPOSSIBLE")

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if (a + b) % 2 == 0:
        print((a + b) // 2)
    else:
        print("IMPOSIBLE")

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    if (A + B) % 2 == 0:
        print((A + B) // 2)
    else:
        print("IMPOSSIBLE")

=======
Suggestion 5

def main():
    # 读取输入
    a, b = map(int, input().split())
    # 判断输出
    if (a+b)%2 != 0:
        print("IMPOSSIBLE")
    else:
        print((a+b)//2)

=======
Suggestion 6

def main():
    a,b = map(int,input().split())
    if (a+b)%2 == 0:
        print(int((a+b)/2))
    else:
        print("IMPOSIBLE")

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    if a < b:
        print(a)
    elif a > b:
        print(b)
    else:
        print("IMPOSSIBLE")
main()

=======
Suggestion 8

def main():
    a,b = map(int, input().split())
    if a == b:
        print("IMPOSSIBLE")
    else:
        print((a+b)//2)

=======
Suggestion 9

def main():
    a,b = map(int,input().split())
    if (a+b)%2==0:
        print(int((a+b)/2))
    else:
        print("IMPOSSIBLE")

=======
Suggestion 10

def solution():
    a,b = map(int, input().split())
    if (a+b)%2 != 0:
        print("IMPOSSIBLE")
    else:
        print((a+b)//2)
