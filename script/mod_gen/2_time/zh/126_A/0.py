def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if a[i] < 0:
            cnt += 1
    if cnt % 2 == 0:
        print(sum(map(abs, a)))
    else:
        print(sum(map(abs, a)) - 2 * min(map(abs, a)))

if __name__ == '__main__':
    main()