Synthesizing 10/10 solutions (Duplicates hidden)

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
    N = int(input())
    sum = 0
    for i in range(N):
        x,u = input().split()
        if u == 'BTC':
            sum += float(x) * 380000.0
        else:
            sum += int(x)
    print(sum)

=======
Suggestion 3

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        x,u = input().split()
        if u == 'BTC':
            sum += float(x) * 380000
        else:
            sum += float(x)
    print(sum)

=======
Suggestion 4

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        a, b = input().split()
        if b == 'BTC':
            sum += float(a) * 380000
        else:
            sum += float(a)
    print(sum)
main()

=======
Suggestion 5

def main():
    n = int(input())
    ans = 0
    for i in range(n):
        x, u = input().split()
        if u == 'BTC':
            ans += float(x) * 380000
        else:
            ans += int(x)
    print(ans)

=======
Suggestion 6

def get_input():
    n = int(input())
    x = []
    u = []
    for i in range(n):
        x_i, u_i = input().split()
        x.append(float(x_i))
        u.append(u_i)
    return n, x, u

=======
Suggestion 7

def main():
    n = int(input())
    x = []
    u = []
    for i in range(n):
        x_i, u_i = input().split()
        x.append(float(x_i))
        u.append(u_i)
    total = 0
    for i in range(n):
        if u[i] == 'BTC':
            total += x[i] * 380000.0
        else:
            total += x[i]
    print(total)

=======
Suggestion 8

def main():
    n = int(input())
    total = 0
    for i in range(n):
        x, u = input().split()
        if u == "BTC":
            total += float(x) * 380000
        else:
            total += int(x)
    print(total)

=======
Suggestion 9

def main():
    n = int(input())
    total = 0
    for i in range(n):
        x,u = input().split()
        if u == 'JPY':
            total += int(x)
        else:
            total += float(x) * 380000.0
    print(total)
