Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    total = 0
    for i in range(n):
        x, u = input().split()
        if u == 'BTC':
            total += float(x) * 380000
        else:
            total += int(x)
    print(total)

=======
Suggestion 2

def main():
    n = int(input())
    x, u = [], []
    for i in range(n):
        x_i, u_i = input().split()
        x.append(float(x_i))
        u.append(u_i)

    print(sum([x_i if u_i == "JPY" else x_i * 380000.0 for x_i, u_i in zip(x, u)]))

=======
Suggestion 3

def main():
    n = int(input())
    x = 0
    for i in range(n):
        tmp = input().split()
        if tmp[1] == "JPY":
            x += int(tmp[0])
        else:
            x += float(tmp[0]) * 380000.0
    print(x)

=======
Suggestion 4

def main():
    n = int(input())
    total = 0
    for i in range(n):
        x, u = input().split()
        if u == 'JPY':
            total += int(x)
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
        if u == "BTC":
            sum += float(x) * 380000.0
        else:
            sum += int(x)
    print(sum)

=======
Suggestion 6

def main():
    n = int(input())
    x = 0
    for i in range(n):
        a, b = input().split()
        if b == 'JPY':
            x += int(a)
        else:
            x += float(a) * 380000.0
    print(x)

=======
Suggestion 7

def main():
    N = int(input())
    x = []
    u = []
    for i in range(N):
        x_i, u_i = input().split()
        x.append(float(x_i))
        u.append(u_i)

    total = 0
    for i in range(N):
        if u[i] == "BTC":
            total += x[i] * 380000.0
        else:
            total += x[i]
    print(total)

=======
Suggestion 8

def main():
    N = int(input())
    ans = 0
    for i in range(N):
        x, u = input().split()
        if u == 'JPY':
            ans += int(x)
        else:
            ans += float(x) * 380000.0
    print(ans)

=======
Suggestion 9

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
main()

=======
Suggestion 10

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
