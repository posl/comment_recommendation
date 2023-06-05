def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    cnt = 1
    max_cnt = 0
    max_str = ""
    for i in range(N-1):
        if S[i] == S[i+1]:
            cnt += 1
        else:
            if max_cnt < cnt:
                max_cnt = cnt
                max_str = S[i]
            cnt = 1
    if max_cnt < cnt:
        max_cnt = cnt
        max_str = S[-1]
    print(max_str)

if __name__ == '__main__':
    main()