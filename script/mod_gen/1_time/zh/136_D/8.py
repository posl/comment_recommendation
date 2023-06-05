def main():
    s = input()
    n = len(s)
    ans = [0] * n
    for i in range(n):
        if s[i] == 'R':
            j = i
            while j < n and s[j] == 'R':
                j += 1
            if (j - i) % 2 == 0:
                ans[j] += 1
            else:
                ans[j-1] += 1
        else:
            j = i
            while j >= 0 and s[j] == 'L':
                j -= 1
            if (i - j) % 2 == 0:
                ans[j] += 1
            else:
                ans[j+1] += 1
    print(' '.join(map(str, ans)))

if __name__ == '__main__':
    main()