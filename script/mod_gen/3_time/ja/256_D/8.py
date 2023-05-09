def main():
    N = int(input())
    LR = []
    for _ in range(N):
        L,R = map(int,input().split())
        LR.append((L,R))
    LR.sort()
    ans = []
    L = LR[0][0]
    R = LR[0][1]
    for l,r in LR:
        if l <= R:
            R = max(R,r)
        else:
            ans.append((L,R))
            L = l
            R = r
    ans.append((L,R))
    for l,r in ans:
        print(l,r)

if __name__ == '__main__':
    main()