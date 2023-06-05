Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        x, u = input().split()
        if u == 'BTC':
            sum += float(x) * 380000
        else:
            sum += int(x)
    print(sum)

=======
Suggestion 2

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        x, u = input().split()
        if u == "BTC":
            sum += float(x) * 380000.0
        else:
            sum += int(x)
    print(sum)

=======
Suggestion 3

def main():
    n = int(input())
    y = 0
    for i in range(n):
        x, u = input().split()
        if u == 'JPY':
            y += int(x)
        else:
            y += float(x) * 380000.0
    print(y)

=======
Suggestion 4

def main():
    n = int(input())
    total = 0
    for i in range(n):
        x, u = input().split()
        if u == 'BTC':
            total += float(x) * 380000.0
        else:
            total += int(x)
    print(total)

=======
Suggestion 5

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        x, u = input().split()
        if u == 'BTC':
            x = float(x)
            x = x * 380000
        else:
            x = int(x)
        sum += x
    print(sum)

=======
Suggestion 6

def main():
    N = int(input())
    sum = 0
    for i in range(N):
        x, u = input().split()
        if u == 'BTC':
            sum += float(x) * 380000
        else:
            sum += int(x)
    print(sum)

=======
Suggestion 7

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        x,u = input().split()
        if u == 'JPY':
            sum += float(x)
        else:
            sum += float(x) * 380000
    print(sum)

=======
Suggestion 8

def calcu_yen(x,u):
    if u == 'BTC':
        return x*380000.0
    else:
        return x

=======
Suggestion 9

def main():
    n = int(input())
    result = 0
    for i in range(n):
        x, u = input().split()
        if u == 'BTC':
            result += float(x) * 380000
        else:
            result += int(x)
    print(result)

=======
Suggestion 10

def problems119_b():
    n = int(input())
    ans = 0
    for i in range(n):
        x, u = input().split()
        if u == 'BTC':
            ans += float(x)*380000
        else:
            ans += int(x)
    print(ans)

problems119_b()
