def main():
    N = int(input())
    P = list(map(int, input().split()))
    #print(N)
    #print(P)
    cnt = 0
    minP = 10**9
    for i in range(N):
        if minP >= P[i]:
            cnt += 1
            minP = P[i]
    print(cnt)
