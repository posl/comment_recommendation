def main():
    N, K = map(int, input().split())
    print(sum([(1/N)*((1/2)**i)*(1/2) for i in range(0,N) if 2**(i+1) >= K]))

if __name__ == '__main__':
    main()