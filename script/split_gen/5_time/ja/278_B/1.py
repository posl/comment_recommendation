def main():
    H, M = map(int, input().split())
    if M < 30:
        H = H - 1
        if H < 0:
            H = 23
        M = M + 30
    else:
        M = M - 30
    print("{0:02d} {1:02d}".format(H, M))
main()
