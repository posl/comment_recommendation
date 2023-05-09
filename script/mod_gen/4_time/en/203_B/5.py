def main():
    N, K = map(int, input().split())
    print(N*100*K*(K+1)//2)

if __name__ == '__main__':
    main()