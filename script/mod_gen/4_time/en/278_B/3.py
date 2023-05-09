def main():
    H,M = map(int, input().split())
    while True:
        if M == 59:
            if H == 23:
                H = 0
                M = 0
            else:
                H += 1
                M = 0
        else:
            M += 1
        if H // 10 == M % 10 and H % 10 == M // 10:
            print(f'{H:02d}:{M:02d}')
            break

if __name__ == '__main__':
    main()