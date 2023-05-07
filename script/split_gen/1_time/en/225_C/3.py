def main():
    N, M = map(int, input().split())
    B = []
    for i in range(N):
        B.append(list(map(int, input().split())))
    for i in range(10**5):
        for j in range(7):
            if B[0][0] == i * 7 + j + 1:
                if i + N > 10**5:
                    print('No')
                    return
                if j + M > 7:
                    print('No')
                    return
                for k in range(N):
                    for l in range(M):
                        if B[k][l] != (i + k) * 7 + (j + l) + 1:
                            print('No')
                            return
                print('Yes')
                return
    print('No')
