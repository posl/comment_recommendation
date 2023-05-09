def main():
    H, M = map(int, input().split())
    if M < 30:
        M = 60 - (30 - M)
        if H == 0:
            H = 23
        else:
            H -= 1
    else:
        M -= 30
    print("{:02d} {:02d}".format(H, M))

if __name__ == '__main__':
    main()