def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    from collections import Counter
    A = Counter(A)
    C = Counter(C)
    ans = 0
    for key in A.keys():
        ans += A[key] * C[B[key]]
    print(ans)

if __name__ == '__main__':
    resolve()