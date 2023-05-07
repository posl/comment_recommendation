def main():
    N = int(input())
    P = list(map(int,input().split()))
    P.insert(0,0)
    #print(P)
    ans = 0
    for i in range(N,1,-1):
        #print(i)
        if P[i] == 1:
            ans = i
            break
        else:
            ans = P[i]
    print(ans)

if __name__ == '__main__':
    main()