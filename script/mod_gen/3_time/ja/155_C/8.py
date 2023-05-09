def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    S.append("")
    now = S[0]
    cnt = 1
    for i in range(1, N + 1):
        if now == S[i]:
            cnt += 1
        else:
            if cnt == max_cnt:
                print(now)
            now = S[i]
            cnt = 1
        max_cnt = max(cnt, max_cnt)

if __name__ == '__main__':
    main()