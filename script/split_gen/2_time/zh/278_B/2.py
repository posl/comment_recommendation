def main():
    H, M = map(int, input().split())
    while True:
        M += 1
        if M == 60:
            H += 1
            M = 0
        if H == 24:
            H = 0
        if str(H) == str(M)[::-1]:
            break
    print(H, M)
