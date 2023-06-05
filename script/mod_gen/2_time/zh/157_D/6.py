def main():
    N,M = map(int,input().split())
    s = [0 for _ in range(M)]
    c = [0 for _ in range(M)]
    for i in range(M):
        s[i],c[i] = map(int,input().split())
    for i in range(10**(N-1),10**N):
        flag = True
        for j in range(M):
            if str(i)[s[j]-1] != str(c[j]):
                flag = False
                break
        if flag:
            print(i)
            break
    else:
        print(-1)

if __name__ == '__main__':
    main()