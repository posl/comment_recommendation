def main():
    s = input()
    k = int(input())
    n = len(s)
    ans = 0
    i = 0
    while i < n:
        if s[i] == 'X':
            i += 1
            continue
        j = i
        while j < n and s[j] == '.':
            j += 1
        ans = max(ans, j - i)
        i = j
    ans = min(ans + k * 2, n)
    print(ans)
