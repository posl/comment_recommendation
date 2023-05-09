def solve(H, M):
    while True:
        if (H%10 == M//10) and (H//10 == M%10):
            return "{}:{}".format(H, M)
        M += 1
        if M == 60:
            M = 0
            H += 1
        if H == 24:
            H = 0

if __name__ == '__main__':
    solve()