def main():
    N, K = map(int, input().split())
    i = 1
    while True:
        if K**i > N:
            print(i)
            return
        i += 1

if __name__ == '__main__':
    main()