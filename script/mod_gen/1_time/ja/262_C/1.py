def main():
    N = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(1, N + 1):
        if a[i - 1] == i:
            cnt += 1
        else:
            cnt += 0
    print(cnt)

if __name__ == '__main__':
    main()