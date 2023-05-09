def main():
    N, M = map(int, input().split())
    A = [0] * (M + 1)
    B = [0] * (M + 1)
    for i in range(1, M + 1):
        A[i], B[i] = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                ans += 1
            else:
                for k in range(1, M + 1):
                    if A[k] == i and B[k] == j:
                        break
                else:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()