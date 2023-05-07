def main():
    H, M = map(int, input().split())
    M += 1
    if M == 60:
        M = 0
        H += 1
        if H == 24:
            H = 0
    while not isConfusing(H, M):
        M += 1
        if M == 60:
            M = 0
            H += 1
            if H == 24:
                H = 0
    print(H, M)
