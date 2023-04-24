Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    total = 0
    for i in range(N):
        x, u = input().split()
        x = float(x)
        if u == "JPY":
            total += x
        else:
            total += x * 380000.0
    print(total)

=======
Suggestion 2

def main():
    N = int(input())
    total = 0
    for i in range(N):
        x, u = input().split()
        x = float(x)
        if u == "JPY":
            total += x
        elif u == "BTC":
            total += x * 380000.0
    print(total)

=======
Suggestion 3

def main():
    N = int(input())
    total = 0
    for i in range(N):
        x, u = input().split()
        if u == 'JPY':
            total += int(x)
        else:
            total += float(x) * 380000.0
    print(total)

=======
Suggestion 4

def main():
    N = int(input())
    total = 0
    for i in range(N):
        x, u = input().split()
        if u == "JPY":
            total += float(x)
        else:
            total += float(x) * 380000.0
    print(total)

=======
Suggestion 5

def main():
    N = int(input())
    sum = 0
    for i in range(N):
        x, u = input().split()
        if u == "JPY":
            sum += int(x)
        else:
            sum += float(x) * 380000.0
    print(sum)

=======
Suggestion 6

def main():
    n = int(input())
    ans = 0
    for i in range(n):
        x, u = input().split()
        if u == "JPY":
            ans += int(x)
        else:
            ans += float(x) * 380000.0
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    sum = 0
    for i in range(N):
        x, u = map(str, input().split())
        x = float(x)
        if u == "JPY":
            sum += x
        else:
            sum += x * 380000.0
    print(sum)

=======
Suggestion 8

def main():
    n = int(input())
    s = 0
    for i in range(n):
        x, u = input().split()
        if u == "JPY":
            s += int(x)
        else:
            s += float(x) * 380000.0
    print(s)
