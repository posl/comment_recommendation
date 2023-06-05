def main():
    N,L = map(int,input().split())
    k = L
    for i in range(1,N+1):
        k += i-1
    if k > 0:
        print(k)
    else:
        print(k+N-1)

if __name__ == '__main__':
    main()