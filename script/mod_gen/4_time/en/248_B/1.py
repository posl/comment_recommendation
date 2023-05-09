def main():
    A, B, K = map(int, input().split())
    cnt = 0
    while A < B:
        cnt += 1
        A *= K
    print(cnt)

if __name__ == '__main__':
    main()