def main():
    N = int(input())
    S = input()
    W = [int(w) for w in input().split()]
    #print(N)
    #print(S)
    #print(W)
    #print(sum(W))
    #print(sum(W[0:3]))
    #print(sum(W[3:5]))
    x = 0
    y = 0
    ans = 0
    for i in range(N):
        if S[i] == '0':
            x += W[i]
        else:
            y += W[i]
    ans = abs(x-y)
    for i in range(N):
        if S[i] == '0':
            x += W[i]
        else:
            y += W[i]
        ans = max(ans,abs(x-y))
    print(ans)

if __name__ == '__main__':
    main()