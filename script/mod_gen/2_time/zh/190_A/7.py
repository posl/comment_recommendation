def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    #print(S)
    #print(type(S))
    count = 0
    for i in range(2**N):
        #print(i)
        #print(type(i))
        x = []
        for j in range(N):
            if (i>>j)&1:
                x.append(True)
            else:
                x.append(False)
        #print(x)
        y = x.copy()
        #print(y)
        for j in range(N):
            if S[j] == "AND":
                y[j] = y[j-1] and x[j]
            elif S[j] == "OR":
                y[j] = y[j-1] or x[j]
        #print(y)
        if y[N-1] == True:
            count += 1
    print(count)

if __name__ == '__main__':
    main()