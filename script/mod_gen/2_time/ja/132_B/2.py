def main():
    n = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    for i in range(1, n-1):
        if p[i-1] < p[i] < p[i+1] or p[i+1] < p[i] < p[i-1]:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()