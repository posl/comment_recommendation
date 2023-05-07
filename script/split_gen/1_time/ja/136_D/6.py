def main():
    s = input()
    n = len(s)
    ans = [0] * n
    ans[0] = 1
    ans[n-1] = 1
    for i in range(1, n-1):
        if s[i] == "R":
            ans[i+1] += 1
        else:
            ans[i-1] += 1
    print(*ans)
