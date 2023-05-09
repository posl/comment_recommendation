def main():
    H,M = map(int,input().split())
    if M < 30:
        H -= 1
        M += 30
    else:
        M -= 30
    if H < 0:
        H += 24
    print(str(H).zfill(2) + " " + str(M).zfill(2))

if __name__ == '__main__':
    main()