def main():
    n = int(input())
    h = list(map(int, input().split()))
    cnt = 0
    max_cnt = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            cnt += 1
        else:
            cnt = 0
        max_cnt = max(cnt, max_cnt)
    print(max_cnt)

if __name__ == '__main__':
    main()