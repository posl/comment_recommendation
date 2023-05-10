def confusing_time(H,M):
    if (H == 0 and M == 0):
        return "00:00"
    if (H == 23 and M == 59):
        return "00:00"
    while True:
        M += 1
        if M == 60:
            M = 0
            H += 1
        if H == 24:
            H = 0
        if H//10 == M%10 and H%10 == M//10:
            return str(H//10) + str(H%10) + ":" + str(M//10) + str(M%10)
H, M = map(int, input().split())
print(confusing_time(H, M))

if __name__ == '__main__':
    confusing_time()