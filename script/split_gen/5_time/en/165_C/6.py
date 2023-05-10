def main():
    N, M, Q = map(int, input().split())
    abcd = []
    for i in range(Q):
        abcd.append(list(map(int, input().split())))
    ans = 0
    for A in list(combinations_with_replacement(range(1, M+1), N)):
        tmp = 0
        for a, b, c, d in abcd:
            if A[b-1] - A[a-1] == c:
                tmp += d
        ans = max(ans, tmp)
    print(ans)
