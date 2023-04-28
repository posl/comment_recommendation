Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, l = map(int, input().split())
    ans = 0
    for i in range(n):
        ans += l + i
    if l < 0 and l + n - 1 >= 0:
        ans -= l + n - 1
    elif l > 0:
        ans -= l
    print(ans)

=======
Suggestion 2

def main():
    N, L = map(int, input().split())
    if L > 0:
        print(int(N*(2*L+N-1)/2 - L))
    elif L+N-1 < 0:
        print(int(N*(2*L+N-1)/2 - L))
    else:
        print(int(N*(2*L+N-1)/2))

=======
Suggestion 3

def main():
    N, L = map(int, input().split())
    ans = 0
    if L >= 0:
        ans = L * N + (N * (N - 1)) // 2 - L
    elif L + N - 1 < 0:
        ans = L * N + (N * (N - 1)) // 2 - L - N + 1
    else:
        ans = L * N + (N * (N - 1)) // 2
    print(ans)

=======
Suggestion 4

def main():
    N, L = map(int, input().split())
    flavor = [L+i-1 for i in range(1, N+1)]
    print(sum(flavor)-min(flavor, key=abs))

=======
Suggestion 5

def main():
    N, L = map(int, input().split())
    sum = 0
    min = 100000000
    for i in range(N):
        sum += L + i
        if abs(L + i) < abs(min):
            min = L + i
    print(sum - min)

=======
Suggestion 6

def main():
    N, L = map(int, input().split())
    print(sum(list(range(L+1, L+N))) - min(range(L+1, L+N), key=lambda x:abs(x)))

=======
Suggestion 7

def main():
    n, l = map(int, input().split())
    if l >= 0:
        print((n-1)*l + (n*(n+1))//2 - (n-1))
    elif l < 0 and l+n-1 >= 0:
        print((n-1)*l + (n*(n+1))//2 - (n-1))
    else:
        print((n-1)*l + (n*(n+1))//2)

=======
Suggestion 8

def main():
    n, l = map(int, input().split())
    apple = [l+i for i in range(n)]
    sum_apple = sum(apple)
    min_apple = min(apple, key=abs)
    print(sum_apple - min_apple)

main()

=======
Suggestion 9

def solve():
    N, L = map(int, input().split())
    print((N * (2 * L + N - 1)) // 2 - L * N)
solve()

=======
Suggestion 10

def problem131_b():
    #print("Input the number of apples and the flavor of the first apple")
    n,l = map(int,input().split())
    #print("The number of apples is %d and the flavor of the first apple is %d" % (n,l))
    sum = 0
    min = 1000
    for i in range(n):
        sum += l+i
        if abs(l+i) < abs(min):
            min = l+i
    print(sum-min)
