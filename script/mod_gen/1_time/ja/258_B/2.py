def main():
    N = int(input())
    A = []
    for _ in range(N):
        A.append(list(map(int, input())))
    ans = 0
    for i in range(N):
        for j in range(N):
            tmp = 0
            for k in range(3):
                for l in range(3):
                    if k == 1 and l == 1:
                        continue
                    tmp += A[(i + k - 1) % N][(j + l - 1) % N] * 10 ** (N - 1)
            ans = max(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()