def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    # print(n, k, r, s, p, t)
    # print(len(t))
    score = 0
    # for i in range(n):
    #     if t[i] == 'r':
    #         score += r
    #     elif t[i] == 's':
    #         score += s
    #     elif t[i] == 'p':
    #         score += p
    # print(score)
    for i in range(n):
        if i < k:
            if t[i] == 'r':
                score += r
            elif t[i] == 's':
                score += s
            elif t[i] == 'p':
                score += p
        else:
            if t[i] == 'r':
                if t[i - k] == 'r':
                    score += 0
                elif t[i - k] == 's':
                    score += s
                elif t[i - k] == 'p':
                    score += p
            elif t[i] == 's':
                if t[i - k] == 'r':
                    score += r
                elif t[i - k] == 's':
                    score += 0
                elif t[i - k] == 'p':
                    score += p
            elif t[i] == 'p':
                if t[i - k] == 'r':
                    score += r
                elif t[i - k] == 's':
                    score += s
                elif t[i - k] == 'p':
                    score += 0
    print(score)

if __name__ == '__main__':
    main()