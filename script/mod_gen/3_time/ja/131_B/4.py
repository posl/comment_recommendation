def main():
    N, L = map(int, input().split())
    print(N*(2*L+N-1)//2-L)

if __name__ == '__main__':
    main()