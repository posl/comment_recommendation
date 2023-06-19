Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort()
    print(sum(p[0:n-1]) + p[n-1] // 2)

=======
Suggestion 2

def solve():
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    p.sort()
    p[-1] = p[-1] / 2
    print(int(sum(p)))

=======
Suggestion 3

def main():
    # 读取输入
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    # 计算
    p.sort()
    p[-1] = p[-1] // 2
    print(sum(p))

=======
Suggestion 4

def main():
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    p.sort()
    p[-1] = p[-1] / 2
    print(int(sum(p)))

=======
Suggestion 5

def problem115_b():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort()
    p[-1] = p[-1] / 2
    print(int(sum(p)))

=======
Suggestion 6

def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort()
    p.reverse()
    p[0] = p[0] / 2
    print(int(sum(p)))

=======
Suggestion 7

def solve():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort(reverse=True)
    s = 0
    for i in range(n):
        if i == 0:
            s += p[i] // 2
        else:
            s += p[i]
    print(s)

=======
Suggestion 8

def main():
    N = int(input())
    p = [0] * N
    for i in range(N):
        p[i] = int(input())
    p.sort(reverse=True)
    p[0] = p[0] / 2
    print(int(sum(p)))

=======
Suggestion 9

def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort()
    p[len(p)-1] = p[len(p)-1] / 2
    print(int(sum(p)))

=======
Suggestion 10

def main():
    n = int(input())
    if n < 2 or n > 10:
        print('N must be 2 <= N <= 10')
        return
    total = 0
    for i in range(n):
        p = int(input())
        if p < 100 or p > 10000:
            print('p must be 100 <= p <= 10000')
            return
        if p % 2 != 0:
            print('p must be even number')
            return
        if p > 10000:
            print('p must be 100 <= p <= 10000')
            return
        total += p
    print(total - int(max(p)/2))
