def main():
    N, M = map(int, input().split())
    if M == 1:
        for i in range(N):
            print(*range(i, i+N))
        return
    if M == 2:
        for i in range(N):
            print(*[0, 1, 1, 2][i%4::4]*(N//4+1)[:N])
        return
    if M == 3:
        for i in range(N):
            print(*[0, 1, 2, 2, 2, 1, 0, 1, 1, 2, 2, 1, 0, 0, 1, 2][i%16::16]*(N//16+1)[:N])
        return
    if M == 4:
        for i in range(N):
            print(*[0, 2, 2, 4][i%4::4]*(N//4+1)[:N])
        return
    if M == 5:
        for i in range(N):
            print(*[0, 1, 2, 3, 3, 2, 1, 0, 1, 2, 3, 4, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 3, 2, 1, 0, 0, 1, 2, 3, 3, 2, 1, 0, 1, 2, 3, 4, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 3, 2, 1, 0, 0, 1, 2, 3, 3, 2, 1, 0, 1, 2, 3, 4, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 3, 2, 1, 0
