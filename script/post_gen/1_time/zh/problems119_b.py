Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_input():
    n = int(input())
    x = []
    u = []
    for i in range(n):
        x_i,u_i = input().split()
        x.append(float(x_i))
        u.append(u_i)
    return n,x,u

=======
Suggestion 2

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
Suggestion 3

def main():
    n = int(input())
    ans = 0
    for i in range(n):
        x, u = input().split()
        if u == 'JPY':
            ans += float(x)
        else:
            ans += float(x) * 380000
    print(ans)

=======
Suggestion 4

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
Suggestion 5

def get_input():
    num = int(input())
    result = 0
    for i in range(num):
        line = input().split()
        if line[1] == "BTC":
            result += float(line[0]) * 380000.0
        else:
            result += int(line[0])
    print(result)

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
            sum += float(x)
    print(sum)

=======
Suggestion 7

def main():
    pass

=======
Suggestion 8

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        x,u = input().split()
        if u == 'JPY':
            sum += int(x)
        else:
            sum += float(x) * 380000.0
    print(sum)

=======
Suggestion 9

def get_input():
    N = int(input())
    x = []
    u = []
    for i in range(N):
        x_u = input().split()
        x.append(float(x_u[0]))
        u.append(x_u[1])
    return N, x, u
