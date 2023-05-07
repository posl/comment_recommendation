def main():
    n, m = map(int, input().split())
    cake = []
    for i in range(n):
        cake.append(list(map(int, input().split())))
    #print(cake)
    
    ans = 0
    for i in range(2**3):
        tmp = []
        for j in range(n):
            tmp.append(cake[j][0] * ((i >> 0) & 1) + cake[j][1] * ((i >> 1) & 1) + cake[j][2] * ((i >> 2) & 1))
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:m]))
    print(ans)

if __name__ == '__main__':
    main()