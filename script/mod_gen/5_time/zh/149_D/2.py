def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    # print(n, k, r, s, p, t)
    score = 0
    for i in range(n):
        if t[i] == 'r':
            score += p
        elif t[i] == 's':
            score += r
        else:
            score += s
    print(score)
    return 0

if __name__ == '__main__':
    main()