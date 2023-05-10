def main():
    N = int(input())
    S = [input() for i in range(N)]
    S.sort()
    max_count = 0
    max_str = ''
    cur_count = 0
    for i in range(N):
        if S[i] == max_str:
            cur_count += 1
        else:
            if cur_count > max_count:
                max_count = cur_count
            max_str = S[i]
            cur_count = 1
    if cur_count > max_count:
        max_count = cur_count
    cur_count = 0
    for i in range(N):
        if S[i] == max_str:
            cur_count += 1
        else:
            if cur_count == max_count:
                print(S[i-1])
            cur_count = 0
            max_str = S[i]
    if cur_count == max_count:
        print(S[i-1])

if __name__ == '__main__':
    main()