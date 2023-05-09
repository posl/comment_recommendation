def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    for i in range(10**5):
        for j in range(7):
            if B[0][0] == i * 7 + j + 1:
                for k in range(N):
                    for l in range(M):
                        if B[k][l] != i * 7 + j + 1 + k * 7 + l:
                            break
                    else:
                        continue
                    break
                else:
                    print("Yes")
                    break
            else:
                continue
        else:
            continue
        break
    else:
        print("No")

if __name__ == '__main__':
    main()