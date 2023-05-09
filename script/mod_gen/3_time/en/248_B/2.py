def main():
    A, B, K = map(int, input().split())
    counter = 0
    while A < B:
        A *= K
        counter += 1
    print(counter)

if __name__ == '__main__':
    main()