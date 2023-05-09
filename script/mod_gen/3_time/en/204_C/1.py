def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                continue
            used = [False] * (N + 1)
            used[i] = True
            used[j] = True
            for k in range(M):
                if A[k] == i:
                    used[B[k]] = True
                if B[k] == i:
                    used[A[k]] = True
            if all(used):
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()