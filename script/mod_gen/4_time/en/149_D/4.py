def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    t = list(t)
    score = 0
    for i in range(n):
        if t[i] == 'r':
            if i >= k:
                if t[i - k] == 'r':
                    t[i] = 'x'
                else:
                    score += r
            else:
                score += r
        elif t[i] == 's':
            if i >= k:
                if t[i - k] == 's':
                    t[i] = 'x'
                else:
                    score += s
            else:
                score += s
        elif t[i] == 'p':
            if i >= k:
                if t[i - k] == 'p':
                    t[i] = 'x'
                else:
                    score += p
            else:
                score += p
    print(score)

if __name__ == '__main__':
    main()