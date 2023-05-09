def main():
    A, B, K = map(int, input().split())
    cnt = 0
    while B > A:
        A *= K
        cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()