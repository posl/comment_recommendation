def main():
    N = int(input())
    W = list(map(int, input().split()))
    #print(N)
    #print(W)
    ans = 1000000000
    for i in range(1, N):
        s1 = sum(W[:i])
        s2 = sum(W[i:])
        #print(s1, s2)
        ans = min(ans, abs(s1 - s2))
    print(ans)

if __name__ == '__main__':
    main()