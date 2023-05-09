Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

def main():
    n = int(input())
    total = 0
    for i in range(n):
        x, u = input().split()
        if u == "JPY":
            total += int(x)
        else:
            total += float(x) * 380000.0
    print(total)

=======
Suggestion 3

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
Suggestion 4

def main():
    N = int(input())
    sum = 0
    for i in range(N):
        x, u = input().split()
        if u == 'JPY':
            sum += int(x)
        else:
            sum += float(x) * 380000.0
    print(sum)

=======
Suggestion 5

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
Suggestion 6

def main():
    N = int(input())
    sum = 0
    for i in range(N):
        x, u = input().split()
        if u == "JPY":
            sum += float(x)
        else:
            sum += float(x)*380000.0
    print(sum)

=======
Suggestion 7

def problems119_b():
    n = int(input())
    sum = 0
    for i in range(n):
        x, u = input().split()
        if u == "JPY":
            sum += int(x)
        else:
            sum += float(x) * 380000.0
    print(sum)

=======
Suggestion 8

def main():
    N = int(input())
    total = 0
    for i in range(N):
        x,u = input().split()
        x = float(x)
        if u == 'BTC':
            total += x * 380000.0
        else:
            total += x
    print(total)

=======
Suggestion 9

def otoshidama(n, x, u):
    sum = 0
    for i in range(n):
        if u[i] == "JPY":
            sum += x[i]
        else:
            sum += x[i] * 380000.0
    return sum

=======
Suggestion 10

def get_input():
    n = int(input())
    x = []
    u = []
    for i in range(n):
        a,b = input().split()
        x.append(float(a))
        u.append(b)
    return n,x,u
