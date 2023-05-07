def main():
    H, M = map(int, input().split())
    if M == 59:
        H += 1
        M = 0
    else:
        M += 1
    if H >= 24:
        H = 0
    print(H, M)

if __name__ == '__main__':
    main()