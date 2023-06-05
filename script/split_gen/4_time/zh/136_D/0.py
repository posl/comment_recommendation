def main():
    s = input()
    n = len(s)
    ans = [0] * n
    i = 0
    while i < n:
        j = i
        while j < n and s[j] == 'R':
            j += 1
        k = j
        while k < n and s[k] == 'L':
            k += 1
        if (j - i) % 2 == 0:
            ans[j - 1] += (j - i) // 2
            ans[j] += (j - i) // 2
        else:
            if (j - i) % 2 == 1:
                ans[j - 1] += (j - i) // 2 + 1
                ans[j] += (j - i) // 2
        i = k
    print(*ans)
