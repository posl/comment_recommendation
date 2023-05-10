def main():
    d, g = map(int, input().split())
    p = [0] * d
    c = [0] * d
    for i in range(d):
        p[i], c[i] = map(int, input().split())
    min_count = 1000
    for i in range(2 ** d):
        count = 0
        score = 0
        unsolved_max = -1
        for j in range(d):
            if i >> j & 1:
                count += p[j]
                score += 100 * (j + 1) * p[j] + c[j]
            else:
                unsolved_max = j
        if score < g:
            if unsolved_max != -1:
                rest = (g - score + 100 * (unsolved_max + 1) - 1) // (100 * (unsolved_max + 1))
                if rest < p[unsolved_max]:
                    count += rest
                else:
                    continue
        if min_count > count:
            min_count = count
    print(min_count)

if __name__ == '__main__':
    main()