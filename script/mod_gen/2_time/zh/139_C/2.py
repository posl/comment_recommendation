def main():
    N = int(input())
    H = list(map(int, input().split()))
    max_cnt = 0
    cnt = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 0
    max_cnt = max(max_cnt, cnt)
    print(max_cnt)

if __name__ == '__main__':
    main()