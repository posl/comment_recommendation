def main():
    n = int(input())
    s = [input() for i in range(n)]
    s = ["".join(sorted(i)) for i in s]
    s = sorted(s)
    ans = 0
    cnt = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            cnt += 1
        else:
            ans += (cnt+1)*cnt//2
            cnt = 0
    ans += (cnt+1)*cnt//2
    print(ans)
