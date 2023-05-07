def main():
    N = int(input())
    X = [None]*N
    Y = [None]*N
    for i in range(N):
        X[i],Y[i] = map(int,input().split())
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if X[i]*(Y[j]-Y[k])+X[j]*(Y[k]-Y[i])+X[k]*(Y[i]-Y[j]) != 0:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()