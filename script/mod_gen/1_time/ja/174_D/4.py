def main():
    N = int(input())
    S = input()
    #print(N)
    #print(S)
    R = S.count('R')
    W = S.count('W')
    ans = 0
    if R==0 or W==0:
        ans = 0
    else:
        ans = min(R,W)
        for i in range(N):
            if S[i]=='R':
                R -= 1
            else:
                W -= 1
            ans = min(ans,R+W)
    print(ans)

if __name__ == '__main__':
    main()