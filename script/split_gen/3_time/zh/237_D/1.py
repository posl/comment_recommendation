def main():
    n = int(input())
    s = input()
    ans = [0] * (n + 1)
    l = 0
    r = n
    for i in range(n):
        if s[i] == 'L':
            ans[l] = i + 1
            l += 1
        else:
            ans[r] = i + 1
            r -= 1
    print(*ans)
