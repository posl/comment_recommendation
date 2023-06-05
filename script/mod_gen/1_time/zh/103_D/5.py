def main():
    N, M = map(int, input().split())
    #print(N, M)
    a = []
    b = []
    for _ in range(M):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    #print(a, b)
    #print(list(zip(a, b)))
    ans = 0
    for i in range(1, N+1):
        #print(i)
        if i in a and i in b:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()