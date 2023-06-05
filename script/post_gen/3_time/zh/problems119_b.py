Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        x, u = input().split()
        x = float(x)
        if u == 'BTC':
            x = x * 380000
        sum += x
    print(sum)

=======
Suggestion 2

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        x, u = input().split()
        if u == 'JPY':
            sum += int(x)
        else:
            sum += float(x) * 380000
    print(sum)

=======
Suggestion 3

def main():
    N = int(input())
    sum = 0
    for i in range(N):
        x, u = input().split()
        if u == 'BTC':
            x = float(x) * 380000
        sum += float(x)
    print(sum)

=======
Suggestion 4

def main():
    n = int(input())
    s = 0
    for i in range(n):
        x, u = input().split()
        if u == 'JPY':
            s += int(x)
        else:
            s += float(x) * 380000.0
    print(s)

=======
Suggestion 5

def main():
    #n = int(input())
    #for i in range(n):
    #    x, u = input().split()
    #    if u == "BTC":
    #        x = float(x) * 380000
    #    print(x)
    n = int(input())
    x = []
    u = []
    for i in range(n):
        x_i, u_i = input().split()
        x.append(float(x_i))
        u.append(u_i)
    sum = 0
    for i in range(n):
        if u[i] == "BTC":
            sum += x[i] * 380000
        else:
            sum += x[i]
    print(sum)

=======
Suggestion 6

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
Suggestion 7

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        x, u = input().split()
        if u == "BTC":
            sum += float(x) * 380000
        else:
            sum += int(x)

    print(sum)

=======
Suggestion 8

def get_input():
    n = int(input())
    x = []
    u = []
    for i in range(n):
        x.append(input())
        u.append(input())
    return n, x, u

=======
Suggestion 9

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
Suggestion 10

def main():
    N = int(input())
    x = []
    u = []
    for i in range(N):
        x1,u1 = input().split()
        x.append(float(x1))
        u.append(u1)
    sum = 0
    for i in range(N):
        if u[i] == 'JPY':
            sum += x[i]
        elif u[i] == 'BTC':
            sum += x[i] * 380000.0
    print(sum)
