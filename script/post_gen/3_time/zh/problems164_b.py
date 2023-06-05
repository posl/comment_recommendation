Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,c,d = map(int,input().split())
    while a>0 and c>0:
        c-=b
        a-=d
    if a<=0:
        print("否")
    else:
        print("是")

main()

=======
Suggestion 2

def main():
    a,b,c,d = map(int, input().split())
    while True:
        c -= b
        if c <= 0:
            print("Yes")
            break
        a -= d
        if a <= 0:
            print("No")
            break

main()

=======
Suggestion 3

def main():
    a,b,c,d = map(int,input().split())
    while True:
        c -= b
        if c <= 0:
            print('Yes')
            break
        a -= d
        if a <= 0:
            print('No')
            break

=======
Suggestion 4

def main():
    a,b,c,d = map(int,input().split())
    while a > 0 and c > 0:
        c -= b
        if c <= 0:
            print("Yes")
            break
        a -= d
        if a <= 0:
            print("No")
            break

=======
Suggestion 5

def main():
    a,b,c,d = map(int,input().split())
    while True:
        c = c - b
        if c <= 0:
            print('Yes')
            break
        a = a - d
        if a <= 0:
            print('No')
            break

=======
Suggestion 6

def main():
    a, b, c, d = map(int, input().split())
    while a > 0 and c > 0:
        c -= b
        a -= d
    print("是" if c <= 0 else "否")
