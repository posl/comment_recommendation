def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input())))
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(8):
                ni = i
                nj = j
                tmp = 0
                for l in range(N):
                    tmp *= 10
                    tmp += A[ni][nj]
                    if k & 1:
                        ni = 2 * i - ni
                    else:
                        ni = 2 * i + ni
                    if k & 2:
                        nj = 2 * j - nj
                    else:
                        nj = 2 * j + nj
                    if ni < 0 or N <= ni or nj < 0 or N <= nj:
                        break
                ans = max(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()