def main():
    N = int(input())
    P = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        if i == P[i]:
            ans += 1
            if i == N-1:
                P[0],P[i] = P[i],P[0]
            else:
                P[i+1],P[i] = P[i],P[i+1]
    print(ans)
main()
