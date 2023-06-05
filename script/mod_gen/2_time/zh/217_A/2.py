def main():
    n, m = map(int, input().split())
    k = [int(input()) for _ in range(m)]
    a = [list(map(int, input().split())) for _ in range(m)]
    cnt = [0] * (n + 1)
    for i in range(m):
        cnt[a[i][0]] += 1
    for i in range(1, n + 1):
        if cnt[i] == 2:
            print("Yes")
            exit()
    print("No")

if __name__ == '__main__':
    main()