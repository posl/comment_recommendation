def main():
    s = input()
    k = int(input())
    n = len(s)
    x = [0] * (n + 1)
    for i in range(n):
        x[i + 1] = x[i] + (s[i] == 'X')
    ans = 0
    for i in range(n + 1):
        l = i
        r = n + 1
        while r - l > 1:
            m = (r + l) // 2
            if x[m] - x[i] > k:
                r = m
            else:
                l = m
        ans = max(ans, l - i)
    print(ans)
