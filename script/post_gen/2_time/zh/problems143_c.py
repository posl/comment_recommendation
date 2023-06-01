Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    d = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            ans += d[i]*d[j]
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    d = list(map(int,input().split()))
    sum = 0
    for i in range(n-1):
        for j in range(i+1,n):
            sum += d[i]*d[j]
    print(sum)

=======
Suggestion 3

def main():
    # 读取输入
    n = int(input())
    d = list(map(int, input().split()))

    # 求和
    sum = 0
    for i in range(n):
        for j in range(i+1, n):
            sum += d[i] * d[j]

    # 输出
    print(sum)

=======
Suggestion 4

def solve():
    N = int(input())
    d = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += d[i] * d[j]
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    d = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        for j in range(i + 1, N):
            sum += d[i] * d[j]
    print(sum)

=======
Suggestion 6

def main():
    n = int(input())
    d = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        for j in range(i+1, n):
            sum += d[i] * d[j]
    print(sum)

=======
Suggestion 7

def main():
    n = int(input())
    d = list(map(int, input().split()))

    total = 0
    for i in range(n):
        for j in range(i+1, n):
            total += d[i] * d[j]

    print(total)

=======
Suggestion 8

def getSumOfHealthPoints(N, d):
    sum = 0
    for i in range(N):
        for j in range(i+1, N):
            sum += d[i] * d[j]

    print(sum)

=======
Suggestion 9

def get_input():
    n = int(input())
    d = list(map(int, input().split()))
    return n, d
