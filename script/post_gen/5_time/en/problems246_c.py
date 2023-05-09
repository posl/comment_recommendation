Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += max(A[i]-K*X, 0)
    print(ans)

=======
Suggestion 2

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if K > 0:
            ans += max(A[i] - X, 0)
            K -= 1
        else:
            ans += A[i]
    print(ans)

=======
Suggestion 3

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))

    total = 0
    for i in range(N):
        total += max(A[i] - K * X, 0)

    print(total)

=======
Suggestion 4

def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(sum([min(x, a[i]) for i in range(n)]))

=======
Suggestion 5

def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(sum([min(x, i) for i in a]))

=======
Suggestion 6

def main():
    n,k,x = map(int, input().split())
    a = list(map(int, input().split()))
    cost = 0
    for i in range(n):
        if k > 0:
            cost += min(a[i],x)
            k -= 1
        else:
            cost += a[i]
    print(cost)

=======
Suggestion 7

def min_cost(N, K, X, A):
    cost = 0
    for i in range(N):
        if K > 0:
            if A[i] > X:
                cost += X
                K -= 1
            else:
                cost += A[i]
        else:
            cost += A[i]
    return cost

=======
Suggestion 8

def problems246_c():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))

    total = 0
    for i in range(N):
        if A[i] - X > 0:
            total += X
        else:
            total += A[i]
    print(total)

=======
Suggestion 9

def main():
    N, K, X = map(int, input().split())
    A_list = list(map(int, input().split()))
    A_list.sort()
    total = 0
    for i in range(N - K):
        total += A_list[i]
    total += K * X
    print(total)

=======
Suggestion 10

def buy_item(a, k, x):
    return max(a - k * x, 0)
