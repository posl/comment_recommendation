def main():
    #input
    N, X = map(int, input().split())
    P = list(map(int, input().split()))
    #output
    print(P.index(X)+1)

if __name__ == '__main__':
    main()