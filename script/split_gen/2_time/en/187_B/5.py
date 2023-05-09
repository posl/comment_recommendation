def main():
    #input
    N = int(input())
    X = [0]*N
    Y = [0]*N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    #compute
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if -1 <= (Y[j]-Y[i])/(X[j]-X[i]) <= 1:
                ans += 1
    #output
    print(ans)
