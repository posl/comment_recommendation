def main():
    n = int(input())
    s = input()
    l = 0
    r = n-1
    ans = [0 for i in range(n)]
    for i in range(n):
        if s[i] == "L":
            ans[r] = i+1
            r -= 1
        else:
            ans[l] = i+1
            l += 1
    print(*ans)
