Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,c = map(int,input().split())
    if a <= b <= c:
        print("是")
    elif c <= b <= a:
        print("是")
    else:
        print("没有")

main()

=======
Suggestion 2

def main():
    a,b,c = map(int, input().split())
    if a<=b<=c or c<=b<=a:
        print("是")
    else:
        print("没有")

=======
Suggestion 3

def is_median(a, b, c):
    if a <= b <= c or c <= b <= a:
        return True
    else:
        return False

a, b, c = map(int, input().split())

=======
Suggestion 4

def main():
    a,b,c = map(int,input().split())
    if b >= a and b <= c or b >= c and b <= a:
        print("是")
    else:
        print("没有")

=======
Suggestion 5

def main():
    a,b,c = map(int,input().split())
    if a<=b<=c or c<=b<=a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    a,b,c = map(int, input().split())
    if b == max(a,b,c) or b == min(a,b,c):
        print("NO")
    else:
        print("YES")

=======
Suggestion 7

def main():
    a,b,c = map(int,input().split())
    if a < b < c or c < b < a:
        print("是")
    else:
        print("否")

=======
Suggestion 8

def main():
    a,b,c = map(int,input().split())
    if b in [a,c]:
        print('是')
    else:
        print('没有')
