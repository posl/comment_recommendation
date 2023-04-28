Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    if B % A == 0:
        print(B // A)
    else:
        print(B // A + 1)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if b % a == 0:
        print(b // a)
    else:
        print(b // a + 1)

=======
Suggestion 3

def solve():
    a, b = map(int, input().split())
    ans = 0
    while b > 0:
        ans += 1
        b -= a - 1
    print(ans)

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    if B % A == 0:
        print(0)
    else:
        print(1)

=======
Suggestion 5

def solve():
    #n = int(input())
    #a, b = map(int, input().split())
    a, b = map(int, input().split())
    #s = input()
    #a = list(map(int, input().split()))
    #b = [input() for _ in range(n)]

    #print(a, b)
    if b == 1:
        print(0)
        return
    n = b - a
    if n < 0:
        print(0)
        return
    print(n + 1)

=======
Suggestion 6

def main():
    a,b = map(int,input().split())
    if b%a == 0:
        print(b//a)
    else:
        print(b//a+1)
main()

=======
Suggestion 7

def calc(a,b):
    cnt = 0
    while True:
        if b <= a:
            break
        b -= (a-1)
        cnt += 1
    return cnt
