def main():
    N,M = map(int,input().split())
    cakes = [list(map(int,input().split())) for _ in range(N)]
    #print(cakes)
    ans = 0
    for i in range(2**3):
        #print(i)
        cake = []
        for j in range(N):
            tmp = 0
            for k in range(3):
                if ((i >> k) & 1):
                    tmp += cakes[j][k]
                else:
                    tmp -= cakes[j][k]
            cake.append(tmp)
        cake.sort(reverse=True)
        #print(cake)
        ans = max(ans,sum(cake[:M]))
    print(ans)

if __name__ == '__main__':
    main()