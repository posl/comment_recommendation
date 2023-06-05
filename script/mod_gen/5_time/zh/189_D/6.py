def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    #print(N)
    #print(S)
    #x = [False]*(N+1)
    #y = [False]*(N+1)
    #x[0] = True
    #y[0] = True
    #for i in range(1,N+1):
    #    if S[i-1] == "AND":
    #        x[i] = x[i-1]
    #    else:
    #        x[i] = not x[i-1]
    #    y[i] = y[i-1] and x[i]
    #print(x)
    #print(y)
    #print(2**N)
    ans = 2**N
    for i in range(N):
        if S[i] == "OR":
            ans += 2**(i+1)
    print(ans)

if __name__ == '__main__':
    main()