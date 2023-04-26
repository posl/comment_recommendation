Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    for i in range(N):
        x, u = input().split()
        if u == "JPY":
            ans += int(x)
        else:
            ans += float(x) * 380000.0
    print(ans)

=======
Suggestion 2

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
    total = 0
    for i in range(N):
        x, u = input().split()
        if u == 'JPY':
            total += int(x)
        else:
            total += float(x) * 380000.0
    print(total)

=======
Suggestion 5

def main():
    n = int(input())
    ans = 0
    for i in range(n):
        x, u = input().split()
        if u == 'JPY':
            ans += int(x)
        else:
            ans += float(x) * 380000.0
    print(ans)

=======
Suggestion 6

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
Suggestion 7

def main():
    N = int(input())
    sum = 0
    for _ in range(N):
        x, u = map(str, input().split())
        if u == "JPY":
            sum += int(x)
        else:
            sum += float(x) * 380000.0
    print(sum)

=======
Suggestion 8

def main():
    #入力
    N = int(input())
    x = []
    u = []
    for i in range(N):
        x_i, u_i = input().split()
        x.append(int(x_i) if u_i == 'JPY' else float(x_i))
        u.append(u_i)

    #計算
    ans = 0
    for i in range(N):
        if u[i] == 'JPY':
            ans += x[i]
        else:
            ans += x[i] * 380000.0

    #出力
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    x = []
    u = []
    for i in range(N):
        x_u = input().split()
        x.append(float(x_u[0]))
        u.append(x_u[1])
    Y = 0.0
    for i in range(N):
        if u[i] == 'JPY':
            Y += x[i]
        else:
            Y += x[i] * 380000.0
    print(Y)

=======
Suggestion 10

def main():
    N = int(input())
    #print(N)
    sum = 0
    for i in range(N):
        x, u = input().split()
        x = float(x)
        #print(x, u)
        if u == "JPY":
            sum += x
        elif u == "BTC":
            sum += x * 380000.0

    print(sum)
