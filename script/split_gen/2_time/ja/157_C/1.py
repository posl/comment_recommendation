def main():
    N, M = map(int, input().split())
    s = [0] * M
    c = [0] * M
    for i in range(M):
        s[i], c[i] = map(int, input().split())
    if M == 0:
        if N == 1:
            print(0)
        else:
            print(10 ** (N - 1))
        return
    else:
        for i in range(10 ** (N - 1), 10 ** N):
            for j in range(M):
                if i // 10 ** (N - s[j]) % 10 == c[j]:
                    if j == M - 1:
                        print(i)
                        return
                else:
                    break
    print(-1)
