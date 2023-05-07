def main():
    N = int(input())
    X = list(map(int,input().split()))
    ans = 0
    for i in range(min(X),max(X)+1):
        temp = 0
        for j in range(N):
            temp += (X[j]-i)**2
        if ans == 0:
            ans = temp
        else:
            ans = min(ans,temp)
    print(ans)

if __name__ == '__main__':
    main()