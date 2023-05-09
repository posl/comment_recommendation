def main():
    N,M = map(int,input().split())
    a = [input().split() for _ in range(M)]
    for i in range(10**N):
        #print(i)
        if len(str(i)) == N:
            for j in range(M):
                if str(i)[int(a[j][0])-1] != a[j][1]:
                    break
                if j == M-1:
                    print(i)
                    return
    print(-1)
    return

if __name__ == '__main__':
    main()