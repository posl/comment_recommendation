def main():
    N,M = map(int,input().split())
    a = [0] * M
    b = [0] * M
    for i in range(M):
        a[i],b[i] = map(int,input().split())
    #print(a)
    #print(b)
    #print(N)
    #print(M)
    #print(a)
    #print(b)
    #print(N)
    #print(M)
    
    print(N-1-M)
    return 0

if __name__ == '__main__':
    main()