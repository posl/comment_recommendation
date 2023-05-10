def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    cnt = 0
    for i in range(1, n + 1):
        if a[a[i]] == i:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()