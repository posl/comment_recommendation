def main():
    n, k = map(int, input().split())
    d = []
    a = []
    for i in range(k):
        d.append(int(input()))
        a.append(list(map(int, input().split())))
    cnt = 0
    for i in range(1, n + 1):
        for j in range(k):
            if i in a[j]:
                break
        else:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()