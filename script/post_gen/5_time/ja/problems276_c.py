Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = [0] * N
    for i in range(N):
        Q[P[i]-1] = i+1
    print(*Q)

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = [0] * n
    for i in range(n):
        q[p[i] - 1] = i + 1
    print(*q)

=======
Suggestion 3

def main():
    N = int(input())
    P = list(map(int,input().split()))
    n = 1
    for i in range(2,N+1):
        n *= i
    for i in range(n):
        if P != list(range(1,N+1)):
            P = P[1:] + [P[0]]
        else:
            break
    print(*P)
main()

=======
Suggestion 4

def main():
    n = int(input())
    p = list(map(int, input().split()))
    p.sort()
    print(*p)

=======
Suggestion 5

def get_permutation(N, K, P):
    # 順列を数値に変換
    P = list(map(lambda x: int(x) - 1, P))
    # 順列を数値に変換
    Q = list(range(N))
    # 順列を数値に変換
    R = list(range(N))
    # 順列を数値に変換
    for i in range(N):
        Q[P[i]] = i
    # 順列を数値に変換
    for i in range(N):
        R[Q[i]] = i
    # 順列を数値に変換
    for i in range(K - 1):
        # 順列を数値に変換
        for j in range(N - 1):
            # 順列を数値に変換
            if R[j] < R[j + 1]:
                # 順列を数値に変換
                R[j], R[j + 1] = R[j + 1], R[j]
                # 順列を数値に変換
                Q[R[j]], Q[R[j + 1]] = Q[R[j + 1]], Q[R[j]]
    return Q

=======
Suggestion 6

def getPermutation(n, k, p):
    ans = [0] * n
    used = [False] * n
    for i in range(n):
        for j in range(n):
            if used[j]:
                continue
            if p[i] == j + 1:
                used[j] = True
                ans[i] = j + 1
                break
    return ans

n = int(input())
p = list(map(int, input().split()))
k = 1
for i in range(n):
    k += math.factorial(n - i - 1) * (p[i] - sum([1 if p[i] > p[j] else 0 for j in range(i)]))
ans = getPermutation(n, k, p)
print(' '.join(map(str, ans)))

=======
Suggestion 7

def get_permutation(n, k):
    if n == 1:
        return [1]
    elif n == 2:
        if k == 1:
            return [1, 2]
        else:
            return [2, 1]
    else:
        if k == 1:
            return [1] + get_permutation(n - 1, 1)
        elif k == 2:
            return [2] + get_permutation(n - 1, 1)
        elif k == 3:
            return [2] + get_permutation(n - 1, 2)
        else:
            return [k - 1] + get_permutation(n - 1, k - 2)

=======
Suggestion 8

def main():
    n = int(input())
    p = list(map(int,input().split()))
    p.insert(0,0)
    q = [0]*n
    for i in range(n):
        q[p[i]-1] = i+1
    print(*q)
