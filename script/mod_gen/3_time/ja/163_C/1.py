def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * n
    for i in range(n-1):
        cnt[a[i]-1] += 1
    for i in range(n):
        print(cnt[i])

if __name__ == '__main__':
    main()