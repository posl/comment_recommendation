def main():
    H, M = map(int, input().split())
    while True:
        if (M + 1) % 60 == 0:
            H = (H + 1) % 24
        M = (M + 1) % 60
        if str(H).zfill(2)[::-1] == str(M).zfill(2):
            break
    print(str(H).zfill(2), str(M).zfill(2))

if __name__ == '__main__':
    main()