def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s.sort()
    res = []
    max_cnt = 0
    cnt = 0
    for i in range(n):
        if s[i] != s[i-1]:
            if cnt > max_cnt:
                max_cnt = cnt
                res = [s[i-1]]
            elif cnt == max_cnt:
                res.append(s[i-1])
            cnt = 1
        else:
            cnt += 1
    if cnt > max_cnt:
        res = [s[-1]]
    elif cnt == max_cnt:
        res.append(s[-1])
    for r in res:
        print(r)

if __name__ == '__main__':
    main()