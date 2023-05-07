def main():
    N = int(input())
    a = list(map(int, input().split()))
    if 1 not in a:
        print(-1)
        return
    if a[0] != 1:
        print(-1)
        return
    count = 0
    now = 1
    for i in range(1, N):
        if a[i] == now + 1:
            now += 1
        else:
            count += 1
    print(count)

if __name__ == '__main__':
    main()