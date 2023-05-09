def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    for i in range(10**4):
        for j in range(7):
            if B[0][0] == (i * 7 + j + 1):
                if N == 1 and M == 1:
                    print("Yes")
                    return
                for k in range(N):
                    for l in range(M):
                        if k == 0 and l == 0:
                            continue
                        if B[k][l] != (i * 7 + j + 1) + (k * 7 + l):
                            break
                    else:
                        continue
                    break
                else:
                    print("Yes")
                    return
    print("No")
