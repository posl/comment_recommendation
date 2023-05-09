def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    for i in range(10**100 - N + 1):
        for j in range(7 - M + 1):
            if B[0][0] == i * 7 + j + 1:
                flag = True
                for k in range(N):
                    for l in range(M):
                        if B[k][l] != (i + k) * 7 + j + l + 1:
                            flag = False
                            break
                    if not flag:
                        break
                if flag:
                    print('Yes')
                    return
    print('No')

if __name__ == '__main__':
    main()