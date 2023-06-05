def main():
    s = input()
    n = len(s)
    ans = [0] * n
    for i in range(n - 1):
        if s[i] == "R" and s[i + 1] == "L":
            ans[i] += 1
            ans[i + 1] += 1
    for i in range(n):
        if s[i] == "R":
            if ans[i] % 2 == 1:
                ans[i + 1] += 1
            ans[i] //= 2
        else:
            if ans[i] % 2 == 1:
                ans[i - 1] += 1
            ans[i] //= 2
    print(*ans)
main()
