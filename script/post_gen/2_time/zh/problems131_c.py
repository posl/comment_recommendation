Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, l = map(int, input().split())
    print(sum(range(l + 1, l + n)) - l if l >= 0 else sum(range(l + 1, l + n)) - l + 1)

=======
Suggestion 2

def solve(n,l):
    return sum(range(l+1,l+n))

=======
Suggestion 3

def main():
    N,L = map(int,input().split())
    sum = 0
    min = 1000
    for i in range(1,N+1):
        sum += L+i-1
        if abs(L+i-1) < abs(min):
            min = L+i-1
    print(sum-min)

=======
Suggestion 4

def main():
    n, l = map(int, input().split())
    if l >= 0:
        print(sum(range(l+1, l+n)))
    elif l+n <= 0:
        print(sum(range(l, l+n)))
    else:
        print(sum(range(l, 0)) + sum(range(1, l+n)))

=======
Suggestion 5

def main():
    n, l = map(int, input().split())
    print(sum(range(l+1, l+n)) if l >= 0 else sum(range(l+1, l+n)) + n - 1)

=======
Suggestion 6

def main():
    N, L = map(int, input().split())
    print((2 * L + N - 1) * N // 2 - L * N)

=======
Suggestion 7

def cal_apple_pie(n,l):
    min_value = 1000000
    for i in range(n):
        temp = 0
        for j in range(n):
            if i != j:
                temp += l + j
        if abs(temp) < min_value:
            min_value = abs(temp)
    return min_value

=======
Suggestion 8

def main():
    n, l = map(int, input().split())
    print(sum(range(l+1, l+n)) if l >= 0 else sum(range(l+n, l+1)))

=======
Suggestion 9

def main():
    N, L = map(int, input().split())
    print(N * L + N * (N - 1) // 2)

=======
Suggestion 10

def main():
    n,l = map(int, input().split())
    res = 0
    if l >= 0:
        res = sum(range(l+1, l+n))
    elif l+n <= 0:
        res = sum(range(l, l+n))
    else:
        res = sum(range(l+1, 0)) + sum(range(1, l+n))
    print(res)
