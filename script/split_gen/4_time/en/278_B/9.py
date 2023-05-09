def confusing_time():
    H, M = map(int, input().split())
    while True:
        if M == 59:
            H += 1
            M = 0
        else:
            M += 1
        if str(H).count('2') + str(M).count('5') == len(str(H)) + len(str(M)):
            print(str(H).zfill(2) + ":" + str(M).zfill(2))
            break
