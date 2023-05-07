def main():
    H, M = map(int, input().split())
    if M == 0:
        print(H, 0)
    else:
        print(H + 1, 0)

if __name__ == '__main__':
    main()