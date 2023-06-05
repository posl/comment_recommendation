def main():
    N = int(input())
    s = []
    for i in range(N):
        s.append(input())
    s.sort()
    s.append('end')
    cnt = 0
    ans = 0
    for i in range(N):
        if s[i] == s[i+1]:
            cnt += 1
        else:
            ans += (cnt+1)*cnt//2
            cnt = 0
    print(ans)
