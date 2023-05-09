def main():
    s = input()
    n = len(s)
    ans = [0] * n
    for i in range(n):
        if s[i] == "R":
            ans[i+1] += 1
        else:
            ans[i] += 1
    for i in range(10**100):
        tmp = [0] * n
        for j in range(n):
            if s[j] == "R":
                tmp[j+1] += ans[j]
            else:
                tmp[j] += ans[j]
        ans = tmp
    print(*ans)
