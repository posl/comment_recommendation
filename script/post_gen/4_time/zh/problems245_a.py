Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,c,d = map(int,input().split())
    if a == c:
        if b == d:
            print("高桥")
        elif b < d:
            print("高桥")
        else:
            print("青木")
    elif a < c:
        print("高桥")
    else:
        print("青木")

=======
Suggestion 2

def main():
    a,b,c,d = map(int,input().split())
    if a<c:
        print("高桥")
    elif a>c:
        print("青木")
    else:
        if b<d:
            print("高桥")
        else:
            print("青木")

main()

=======
Suggestion 3

def main():
    a,b,c,d = map(int,input().split())
    if a*60+b<c*60+d:
        print("高桥")
    else:
        print("青木")

=======
Suggestion 4

def main():
    # 读取输入
    a, b, c, d = map(int, input().split())
    # 比较
    if a < c:
        print("高桥")
    elif a > c:
        print("青木")
    else:
        if b < d:
            print("高桥")
        elif b > d:
            print("青木")
        else:
            print("高桥")

=======
Suggestion 5

def main():
    a,b,c,d = map(int,input().split())
    if a > c:
        print("高桥")
    elif a == c and b > d:
        print("高桥")
    else:
        print("青木")

=======
Suggestion 6

def main():
    a,b,c,d = map(int, input().split())
    if a < c:
        print("高桥")
    elif a == c:
        if b <= d:
            print("高桥")
        else:
            print("青木")
    else:
        print("青木")

=======
Suggestion 7

def problem245_a():
    a,b,c,d = map(int,input().split())
    if a*60+b < c*60+d:
        print("高桥")
    else:
        print("青木")

problem245_a()

=======
Suggestion 8

def main():
    A, B, C, D = map(int, input().split())
    t1 = A * 60 + B
    t2 = C * 60 + D
    if t1 < t2:
        print("青木")
    else:
        print("高桥")
main()

=======
Suggestion 9

def main():
    a,b,c,d=map(int,input().split())
    if a<c:
        print("高桥")
    elif a>c:
        print("青木")
    else:
        if b<d:
            print("高桥")
        else:
            print("青木")
