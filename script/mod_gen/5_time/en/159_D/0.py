def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = {}
    for i in a:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
    total = 0
    for i in cnt:
        total += cnt[i] * (cnt[i] - 1) // 2
    for i in a:
        print(total - (cnt[i] - 1))

if __name__ == '__main__':
    main()