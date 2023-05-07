def main():
    n, m = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(n)]
    for i in range(10 ** 100 - n + 1):
        for j in range(7 - m + 1):
            if b[0][0] == i * 7 + j + 1:
                for k in range(n):
                    for l in range(m):
                        if b[k][l] != i * 7 + j + k * 7 + l + 1:
                            break
                    else:
                        continue
                    break
                else:
                    print('Yes')
                    return
    print('No')
