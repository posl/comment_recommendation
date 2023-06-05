def main():
    s = input()
    n = len(s)
    ans = [0] * n
    for i in range(n):
        if s[i] == 'R' and s[i + 1] == 'L':
            r = i
            l = i + 1
            while s[r] == 'R':
                r -= 1
            while s[l] == 'L':
                l += 1
            if (r - i) % 2 == 0 and (i - l) % 2 == 0:
                ans[i] += 1
            elif (r - i) % 2 != 0 and (i - l) % 2 != 0:
                ans[i + 1] += 1
            elif (r - i) % 2 == 0 and (i - l) % 2 != 0:
                ans[i] += 1
                ans[i + 1] += 1
            elif (r - i) % 2 != 0 and (i - l) % 2 == 0:
                ans[i] += 1
                ans[i + 1] += 1
    print(*ans)
