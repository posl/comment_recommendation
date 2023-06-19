Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    #输入
    N = int(input())
    x = []
    u = []
    for i in range(N):
        x_u = input().split()
        x.append(float(x_u[0]))
        u.append(x_u[1])
    #处理
    sum = 0
    for i in range(N):
        if u[i] == 'BTC':
            sum += x[i] * 380000
        elif u[i] == 'JPY':
            sum += x[i]
    #输出
    print(sum)

=======
Suggestion 2

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        x, u = input().split()
        if u == 'BTC':
            x = float(x) * 380000
        sum += float(x)
    print(sum)

=======
Suggestion 3

def main():
    N = int(input())
    total = 0
    for i in range(N):
        x, u = input().split()
        if u == "BTC":
            total += float(x)*380000.0
        else:
            total += int(x)
    print(total)

=======
Suggestion 4

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        x, u = input().split()
        if u == "JPY":
            sum += int(x)
        else:
            sum += float(x)*380000
    print(sum)

=======
Suggestion 5

def solve():
    n = int(input())
    ans = 0
    for i in range(n):
        x, u = input().split()
        if u == "JPY":
            ans += int(x)
        else:
            ans += float(x) * 380000
    print(ans)
solve()

=======
Suggestion 6

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        x,u = input().split()
        if u == 'JPY':
            sum += int(x)
        else:
            sum += float(x)*380000.0
    print(sum)

main()

=======
Suggestion 7

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        x, u = input().split()
        if u == 'BTC':
            sum += 380000.0 * float(x)
        else:
            sum += float(x)
    print(sum)

=======
Suggestion 8

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
Suggestion 9

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        x, u = input().split()
        if u == 'JPY':
            sum += int(x)
        else:
            sum += float(x) * 380000.0
    print(sum)
