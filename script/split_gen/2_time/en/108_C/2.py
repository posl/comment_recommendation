def main():
    N, K = map(int, input().split())
    cnt = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if (i + j) % K == 0 and (j + k) % K == 0 and (k + i) % K == 0:
                    cnt += 1
    print(cnt)
