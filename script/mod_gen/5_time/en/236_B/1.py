def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * (n + 1)
    for i in a:
        cnt[i] += 1
    for i in range(1, n + 1):
        if cnt[i] % 2 == 1:
            print(i)
            return

if __name__ == '__main__':
    main()