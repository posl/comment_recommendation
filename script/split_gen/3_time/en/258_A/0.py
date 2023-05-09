def main():
    K = int(input())
    H = 21
    M = 0
    M += K
    if M > 59:
        H += M // 60
        M = M % 60
    if H > 23:
        H = H % 24
    print(str(H).zfill(2) + ':' + str(M).zfill(2))
