def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i - 1 for i in a]
    flag = [False] * n
    flag[x - 1] = True
    count = 1
    while True:
        for i in range(n):
            if flag[i]:
                continue
            if a[i] == x - 1:
                flag[i] = True
                count += 1
        if False not in flag:
            break
        x = a[x - 1] + 1
    print(count)

if __name__ == '__main__':
    main()