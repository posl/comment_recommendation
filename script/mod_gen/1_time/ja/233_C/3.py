def main():
    N, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    #print(N, X)
    #print(A)
    ans = 0
    for i in range(1, 2**N):
        #print("i:", i)
        tmp = 1
        for j in range(N):
            if i & 1 << j:
                #print("j:", j)
                tmp *= A[j][0]
        #print("tmp:", tmp)
        if tmp > X:
            continue
        #print("i:", i)
        for j in range(N):
            if i & 1 << j:
                #print("j:", j)
                for k in range(1, A[j][0]+1):
                    #print("k:", k)
                    if tmp * A[j][k] == X:
                        ans += 1
                    elif tmp * A[j][k] > X:
                        break
    print(ans)

if __name__ == '__main__':
    main()