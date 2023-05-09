def main():
    N, M = map(int, input().split())
    if M == 0:
        print(3**N)
    else:
        print(0)

if __name__ == '__main__':
    main()