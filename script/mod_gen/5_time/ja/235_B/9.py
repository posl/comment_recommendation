def main():
    N = int(input())
    H = list(map(int, input().split()))
    cnt = 0
    max_cnt = 0
    for i in range(1,N):
        if H[i-1] >= H[i]:
            cnt += 1
        else:
            cnt = 0
        if max_cnt < cnt:
            max_cnt = cnt
    print(max_cnt)

if __name__ == '__main__':
    main()