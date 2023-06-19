def main():
    K = int(input())
    H = 21
    M = 0
    for i in range(K):
        M += 1
        if M == 60:
            M = 0
            H += 1
            if H == 24:
                H = 0
    if H < 10:
        print("0", end = "")
    print(H, end = ":")
    if M < 10:
        print("0", end = "")
    print(M)

if __name__ == '__main__':
    main()