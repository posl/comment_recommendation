def main():
    s = input()
    n = len(s)
    ans = [0]*n
    for i in range(n):
        if s[i] == "R":
            if s[i+1] == "R":
                ans[i+2] += ans[i]
                ans[i] = 0
            else:
                ans[i+1] += ans[i]
                ans[i] = 0
        else:
            if s[i-1] == "L":
                ans[i-2] += ans[i]
                ans[i] = 0
            else:
                ans[i-1] += ans[i]
                ans[i] = 0
    print(*ans)
