def main():
    # input
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    # process
    cnt = 0
    for i in range(n):
        if a[i] < p:
            cnt += 1
    # output
    print(cnt)

if __name__ == '__main__':
    main()