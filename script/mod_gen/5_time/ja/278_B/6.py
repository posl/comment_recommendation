def main():
    H, M = map(int, input().split())
    if M < 30:
        H -= 1
        M += 30
    else:
        M -= 30
    print("{0:02d} {1:02d}".format(H, M))

if __name__ == '__main__':
    main()