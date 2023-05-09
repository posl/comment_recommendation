def main():
    A, B, K = map(int, input().split())
    count = 0
    while True:
        if A >= B:
            break
        A *= K
        count += 1
    print(count)

if __name__ == '__main__':
    main()