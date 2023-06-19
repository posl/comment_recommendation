def solve():
    n,k = map(int,input().split())
    s = input()
    s = s.replace("LR","L R")
    s = s.replace("RL","R L")
    #print(s)
    s = s.split()
    #print(s)
    ans = 0
    for i in range(len(s)):
        if s[i][0] == "L":
            ans += 1
        if s[i][-1] == "R":
            ans += 1
    ans = min(ans+2*k,n)
    print(ans)

if __name__ == '__main__':
    solve()