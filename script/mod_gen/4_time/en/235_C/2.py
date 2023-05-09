def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for _ in range(q):
        x, k = map(int, input().split())
        cnt = 0
        for i in range(n):
            if a[i] == x:
                cnt += 1
            if cnt == k:
                print(i+1)
                break
        else:
            print(-1)

if __name__ == '__main__':
    main()