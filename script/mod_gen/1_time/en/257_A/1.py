def main():
    N, X = map(int, input().split())
    if X <= N:
        print(chr(64+X))
    else:
        X -= N
        print(chr(64+X//N+1))

if __name__ == '__main__':
    main()