def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    A.sort()
    A.append(10**18 + 1)
    res = []
    j = 0
    for k in K:
        while k > 0:
            if A[j+1] - A[j] - 1 >= k:
                res.append(A[j] + k)
                break
            else:
                k -= A[j+1] - A[j] - 1
                j += 1
    print('\n'.join(map(str, res)))
