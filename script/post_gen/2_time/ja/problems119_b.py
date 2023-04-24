Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    Y = 0
    for i in range(N):
        x, u = input().split()
        x = float(x)
        if u == "JPY":
            Y += x
        else:
            Y += x * 380000.0
    print(Y)

=======
Suggestion 2

def main():
    n = int(input())
    ans = 0
    for i in range(n):
        x, u = input().split()
        x = float(x)
        if u == "JPY":
            ans += x
        else:
            ans += x * 380000.0
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    total = 0
    for i in range(N):
        x, u = input().split()
        x = float(x)
        if u == 'JPY':
            total += x
        else:
            total += x * 380000.0
    print(total)

=======
Suggestion 4

def main():
    n = int(input())
    total = 0
    for i in range(n):
        x, u = input().split()
        x = float(x)
        if u == "JPY":
            total += x
        else:
            total += x * 380000.0
    print(total)

=======
Suggestion 5

def main():
    n = int(input())
    total = 0
    for i in range(n):
        x, u = input().split()
        x = float(x)
        if u == 'JPY':
            total += x
        else:
            total += x * 380000
    print(total)

=======
Suggestion 6

def main():
    N = int(input())
    sum = 0
    for i in range(N):
        x, u = input().split()
        x = float(x)
        if u == "JPY":
            sum += x
        else:
            sum += x * 380000.0
    print(sum)

=======
Suggestion 7

def main():
    N = int(input())
    ans = 0
    for _ in range(N):
        x, u = input().split()
        if u == 'JPY':
            ans += int(x)
        else:
            ans += float(x) * 380000.0
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        x, u = input().split()
        if u == "JPY":
            sum += int(x)
        else:
            sum += float(x) * 380000
    print(sum)

=======
Suggestion 9

def main():
    N = int(input())
    money = 0
    for i in range(N):
        x, u = input().split()
        if u == "JPY":
            money += int(x)
        else:
            money += float(x) * 380000.0
    print(money)

=======
Suggestion 10

def solve():
    N = int(input())
    ans = 0
    for i in range(N):
        x, u = input().split()
        x = float(x)
        if u == 'JPY':
            ans += x
        else:
            ans += x * 380000.0
    print(ans)
    return
