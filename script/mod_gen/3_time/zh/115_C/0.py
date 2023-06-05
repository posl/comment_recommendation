def main():
    n,k = map(int,input().split())
    h = [int(input()) for i in range(n)]
    h.sort()
    min = 10**9
    for i in range(n-k+1):
        if h[i+k-1]-h[i] < min:
            min = h[i+k-1]-h[i]
    print(min)

if __name__ == '__main__':
    main()