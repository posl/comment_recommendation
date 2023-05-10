def confusing_time(H, M):
    while True:
        M += 1
        if M == 60:
            M = 0
            H += 1
        if H == 24:
            H = 0
        if H // 10 == M % 10 and H % 10 == M // 10:
            return H, M
H, M = map(int, input().split())
h, m = confusing_time(H, M)
print(h, m)
