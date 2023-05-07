def main():
    N = int(input())
    P = []
    for i in range(N):
        x,y = map(int,input().split())
        P.append((x,y))
    P.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            x1,y1 = P[i]
            x2,y2 = P[j]
            if x1==x2 or y1==y2:
                continue
            if (x1,y2) in P and (x2,y1) in P:
                ans += 1
    print(ans)
