def main():
    # A,B,K = map(int, input().split())
    A,B,K = 31,415926,5
    count = 0
    while A < B:
        A *= K
        count += 1
    print(count)

if __name__ == '__main__':
    main()