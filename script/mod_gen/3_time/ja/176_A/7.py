def main():
    N, X, T = map(int, input().split())
    print(((N-1)//X+1)*T)

if __name__ == '__main__':
    main()