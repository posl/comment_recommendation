def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    print(max([sum(p[i:i+k])*(p[i+k-1]+1)/2 for i in range(n-k+1)]))

if __name__ == '__main__':
    main()