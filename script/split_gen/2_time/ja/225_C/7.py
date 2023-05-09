def main():
    N, M = map(int, input().split())
    B = []
    for _ in range(N):
        B.append(list(map(int, input().split())))
    for i in range(10**100 - N + 1):
        for j in range(7 - M + 1):
            if B[0][0] == i * 7 + j + 1:
                for k in range(N):
                    for l in range(M):
                        if B[k][l] != i * 7 + j + k * 7 + l + 1:
                            break
                    else:
                        continue
                    break
                else:
                    print("Yes")
                    return
    print("No")
    return
