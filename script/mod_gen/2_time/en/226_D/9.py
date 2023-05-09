def main():
    N = int(input())
    X,Y = [],[]
    for i in range(N):
        a,b = map(int,input().split())
        X.append(a)
        Y.append(b)
    ans = set()
    for i in range(N):
        for j in range(i+1,N):
            ans.add((X[i]-X[j],Y[i]-Y[j]))
            ans.add((X[j]-X[i],Y[j]-Y[i]))
    print(len(ans))
main()

if __name__ == '__main__':
    main()