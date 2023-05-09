def main():
    N, K = map(int, input().split())
    cnt = 0
    for a in range(1, N+1):
        for b in range(1, N+1):
            if (a+b)%K == 0:
                for c in range(1, N+1):
                    if (b+c)%K == 0 and (c+a)%K == 0:
                        cnt += 1
    print(cnt)
