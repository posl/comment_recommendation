def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if a[i] < 0:
            cnt += 1
            a[i] = -a[i]
    if cnt % 2 == 0:
        print(sum(a))
    else:
        print(sum(a) - 2 * min(a))

if __name__ == '__main__':
    main()