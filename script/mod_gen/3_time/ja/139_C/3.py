def main():
    N = int(input())
    H = list(map(int, input().split()))
    cnt = 0
    max_cnt = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
        else:
            cnt = 0
    print(max_cnt)

if __name__ == '__main__':
    main()