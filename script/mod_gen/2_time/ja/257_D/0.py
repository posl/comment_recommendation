def main():
    N = int(input())
    x = [0 for i in range(N)]
    y = [0 for i in range(N)]
    P = [0 for i in range(N)]
    for i in range(N):
        x[i],y[i],P[i] = map(int,input().split())
    S = 0
    for i in range(N):
        for j in range(N):
            if P[i]*S >= abs(x[i]-x[j]) + abs(y[i]-y[j]):
                S = S + 1
    print(S)
main()
