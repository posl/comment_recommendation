def main():
    n, m, q = map(int, input().split())
    abcd = [list(map(int, input().split())) for _ in range(q)]
    # print(n, m, q)
    # print(abcd)
    A = [1] * n
    # print(A)
    ans = 0
    while True:
        # print(A)
        tmp = 0
        for a, b, c, d in abcd:
            if A[b-1] - A[a-1] == c:
                tmp += d
        ans = max(ans, tmp)
        A[0] += 1
        if A[0] > m:
            for i in range(1, n):
                if A[i-1] < m:
                    A[i-1] += 1
                    for j in range(i-1):
                        A[j] = A[i-1]
                    break
            else:
                break
    print(ans)
