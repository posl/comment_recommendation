def main():
    H, M = map(int, input().split())
    if M == 59:
        H += 1
        M = 0
    else:
        M += 1
    print(str(H).zfill(2), str(M).zfill(2))

if __name__ == '__main__':
    main()