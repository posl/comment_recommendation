def main():
    n = int(input())
    s = input()
    #print(n, s)
    r = 0
    g = 0
    b = 0
    for i in range(n):
        if s[i] == 'R':
            r += 1
        elif s[i] == 'G':
            g += 1
        else:
            b += 1
    #print(r, g, b)
    ans = r * g * b
    for i in range(n):
        for j in range(i + 1, n):
            k = j + j - i
            if k >= n:
                break
            if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                ans -= 1
    print(ans)

if __name__ == '__main__':
    main()