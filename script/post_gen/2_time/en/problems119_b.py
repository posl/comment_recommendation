Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    total = 0
    for i in range(N):
        x, u = input().split()
        if u == "JPY":
            total += int(x)
        else:
            total += float(x) * 380000.0
    print(total)

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(N):
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
        if u == "JPY":
            total += float(x)
        else:
            total += float(x) * 380000.0
    print(total)

=======
Suggestion 4

def main():
    N = int(input())
    sum = 0
    for i in range(N):
        x, u = input().split()
        x = float(x)
        if u == 'JPY':
            sum += x
        else:
            sum += x * 380000
    print(sum)

=======
Suggestion 5

def main():
    N = int(input())
    Y = 0
    for i in range(N):
        x, u = input().split()
        x = float(x)
        if u == 'JPY':
            Y += x
        else:
            Y += x*380000.0
    print(Y)

=======
Suggestion 6

def main():
    n = int(input())
    total = 0.0
    for i in range(n):
        x, u = input().split()
        x = float(x)
        if u == "JPY":
            total += x
        else:
            total += x * 380000.0
    print(total)

=======
Suggestion 7

def main():
    N = int(input())
    total = 0
    for i in range(N):
        x, u = map(str, input().split())
        if u == "JPY":
            total += int(x)
        else:
            total += float(x) * 380000.0
    print(total)

main()

=======
Suggestion 8

def main():
    N = int(input())
    total = 0
    for _ in range(N):
        x, u = input().split()
        if u == 'JPY':
            total += float(x)
        elif u == 'BTC':
            total += float(x) * 380000.0
    print(total)

main()

=======
Suggestion 9

def main():
    N = int(input())
    BTC = 380000.0
    total = 0
    for i in range(N):
        x, u = input().split()
        x = float(x)
        if u == 'JPY':
            total += x
        else:
            total += x * BTC
    print(total)
