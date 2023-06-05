def main():
    N = int(input())
    P = list(map(int, input().split()))
    P.insert(0, 0)
    P.append(0)
    #print(P)
    ans = 0
    for i in range(1, N+1):
        if P[i-1] < P[i] < P[i+1] or P[i+1] < P[i] < P[i-1]:
            ans += 1
    print(ans)
