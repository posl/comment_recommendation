Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, l = map(int, input().split())
    sum = 0
    for i in range(1, n+1):
        sum += l + i - 1
    if l + n - 1 > 0:
        sum -= l + n - 1
    elif l < 0:
        sum -= l
    print(sum)

=======
Suggestion 2

def main():
    N,L = map(int,input().split())
    ans = 0
    min_diff = 1000000000
    for i in range(N):
        ans += L + i
        if abs(L+i) < min_diff:
            min_diff = abs(L+i)
            min_index = i
    print(ans - (L + min_index))

=======
Suggestion 3

def main():
    n,l = map(int,input().split())
    min_sum = 1000000000
    for i in range(1,n+1):
        if abs(l+i-1) < abs(min_sum):
            min_sum = l+i-1
    print(sum(range(l+1,l+n))-min_sum)

=======
Suggestion 4

def main():
    N, L = map(int, input().split())

    sum = 0
    for i in range(1, N+1):
        sum += L + i - 1

    if L >= 0:
        print(sum - L)
    elif L + N - 1 < 0:
        print(sum - L - N + 1)
    else:
        print(sum)

=======
Suggestion 5

def solve():
    N,L = map(int, input().split())
    if N == 1:
        print(L)
        return
    if L >= 0:
        print(sum(range(L+1, L+N)))
        return
    if L+N-1 <= 0:
        print(sum(range(L, L+N-1)))
        return
    print((L+N-1)*N//2)

solve()

=======
Suggestion 6

def main():
    n,l = map(int,input().split())
    if l > 0:
        print(sum(range(l+1,l+n)))
    elif l+n-1 < 0:
        print(sum(range(l,l+n-1)))
    else:
        print(sum(range(l,l+n)))

=======
Suggestion 7

def main():
    n,l = map(int,input().split())
    print((n*l)+(n*(n-1)//2))

=======
Suggestion 8

def main():
    N,L = map(int,input().split())
    print(sum(range(L+1,L+N)))

=======
Suggestion 9

def main():
    n,l = map(int,input().split())
    min_sum = 1000000000
    for i in range(1,n+1):
        if min_sum > abs(l+i-1):
            min_sum = abs(l+i-1)
            min_index = i
    sum = 0
    for i in range(1,n+1):
        if i != min_index:
            sum += l+i-1
    print(sum)

=======
Suggestion 10

def main():
    n,l = map(int,input().split())
    min_value = 1000
    for i in range(n):
        if min_value > abs(l+i):
            min_value = abs(l+i)
            index = i
    if l > 0:
        print(sum(range(l+1,l+n)))
    elif l+n-1 < 0:
        print(sum(range(l,l+n-1,-1)))
    else:
        print(sum(range(l,l+n))-index)
main()
