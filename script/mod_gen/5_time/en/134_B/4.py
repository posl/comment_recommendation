def main():
    N, D = map(int, input().split())
    print(int(N/(D*2+1))+1 if N%(D*2+1) != 0 else int(N/(D*2+1)))

if __name__ == '__main__':
    main()