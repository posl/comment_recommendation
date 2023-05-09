def main():
    n, m = map(int, input().split())
    p = [0 for i in range(n)]
    s = [0 for i in range(n)]
    for i in range(m):
        p_, s_ = map(str, input().split())
        p_ = int(p_)
        p[p_-1] += 1
        if s_ == 'AC':
            s[p_-1] = 1
    sum_p = 0
    sum_s = 0
    for i in range(n):
        if s[i] == 1:
            sum_p += p[i]
            sum_s += 1
    print(sum_s, sum_p)

if __name__ == '__main__':
    main()