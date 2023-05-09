def main():
    N = int(input())
    a = list(map(int, input().split()))
    if N == 1:
        if a[0] == 1:
            print(0)
        else:
            print(-1)
        return
    if a[0] != 1:
        print(-1)
        return
    count = 0
    for i in range(1, N):
        if a[i] - a[i - 1] == 1:
            continue
        elif a[i] - a[i - 1] == 0:
            count += 1
        else:
            print(-1)
            return
    print(count)

if __name__ == '__main__':
    main()