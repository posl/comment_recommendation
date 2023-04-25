Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

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
Suggestion 3

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

main()

=======
Suggestion 4

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
Suggestion 5

def main():
    N = int(input())
    total = 0.0
    for i in range(N):
        x, u = input().split()
        x = float(x)
        if u == 'JPY':
            total += x
        else:
            total += x * 380000.0
    print(total)

=======
Suggestion 6

def main():
    N = int(input())
    total = 0.0
    for _ in range(N):
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
    #input
    N = int(input())
    xus = [input().split() for _ in range(N)]

    #compute
    ans = 0
    for xu in xus:
        x, u = xu
        x = float(x)
        if u == 'JPY':
            ans += x
        else:
            ans += x * 380000.0

    #output
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    X = []
    U = []
    for i in range(N):
        x, u = input().split()
        X.append(float(x))
        U.append(u)
    sum = 0.0
    for i in range(N):
        if U[i] == 'JPY':
            sum += X[i]
        else:
            sum += X[i] * 380000.0
    print(sum)

=======
Suggestion 9

def main():
    N = int(input())
    x = []
    u = []
    for _ in range(N):
        x_, u_ = input().split()
        x.append(float(x_))
        u.append(u_)
    
    ans = 0
    for i in range(N):
        if u[i] == 'JPY':
            ans += x[i]
        elif u[i] == 'BTC':
            ans += x[i] * 380000.0
    
    print(ans)
