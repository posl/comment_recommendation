def main():
    n = int(input())
    s = input()
    r_count = 0
    g_count = 0
    b_count = 0
    for i in range(n):
        if s[i] == 'R':
            r_count += 1
        elif s[i] == 'G':
            g_count += 1
        else:
            b_count += 1
    total = r_count * g_count * b_count
    for i in range(n):
        for j in range(i+1, n):
            k = 2 * j - i
            if k >= n:
                continue
            if s[i] == s[j]:
                continue
            if s[i] == s[k]:
                continue
            if s[j] == s[k]:
                continue
            total -= 1
    print(total)

if __name__ == '__main__':
    main()