def main():
    H,M = map(int,input().split())
    M = M + 60
    if M > 59:
        H = H + 1
        M = M - 60
    if H > 23:
        H = H - 24
    print(str(H).zfill(2), str(M).zfill(2))
