Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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

main()

=======
Suggestion 2

def main():
    n = int(input())
    ans = 0
    for _ in range(n):
        x, u = input().split()
        if u == 'BTC':
            ans += float(x) * 380000
        else:
            ans += int(x)
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    sum = 0
    for i in range(N):
        x, u = input().split()
        if u == 'BTC':
            sum += float(x) * 380000.0
        else:
            sum += int(x)
    print(sum)

=======
Suggestion 4

def main():
    n = int(input())
    y = 0
    for i in range(n):
        x, u = input().split()
        if u == 'BTC':
            y += float(x) * 380000
        else:
            y += int(x)
    print(y)

=======
Suggestion 5

def main():
    n = int(input())
    ans = 0
    for i in range(n):
        x, u = input().split()
        if u == 'BTC':
            ans += float(x)*380000.0
        else:
            ans += int(x)
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    x = []
    u = []
    for i in range(n):
        x_i, u_i = input().split()
        x.append(float(x_i))
        u.append(u_i)

    y = 0
    for i in range(n):
        if u[i] == 'BTC':
            y += x[i] * 380000.0
        else:
            y += x[i]
    print(y)

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

    ans = 0
    for i in range(N):
        if u[i] == 'BTC':
            ans += x[i] * 380000
        else:
            ans += x[i]
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    x = []
    u = []
    for i in range(N):
        x_i, u_i = input().split()
        x.append(float(x_i))
        u.append(u_i)

    ans = 0
    for i in range(N):
        if u[i] == "JPY":
            ans += x[i]
        else:
            ans += x[i] * 380000

    print(ans)

main()

=======
Suggestion 9

def main():
    n = int(input())
    x = []
    u = []
    for i in range(n):
        x_u = input().split()
        x.append(float(x_u[0]))
        u.append(x_u[1])

    y = 0
    for i in range(n):
        if u[i] == "JPY":
            y += x[i]
        else:
            y += x[i] * 380000.0

    print(y)

main()
