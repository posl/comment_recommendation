def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(0)
    A.insert(0, 0)
    for i in range(1, N + 2):
        for j in range(i + 1, N + 2):
            if i == j:
                continue
            for k in range(j + 1, N + 2):
                if k == j:
                    continue
                if i == k:
                    continue
                if (A[i] * A[i] + A[j] * A[j] == A[k] * A[k]) and (i == 1 or j == 1 or k == 1 or i == N + 1 or j == N + 1 or k == N + 1):
                    print('Yes')
                    return
    print('No')
    return

if __name__ == '__main__':
    main()