def main():
    #input
    L, R = map(int, input().split())
    #compute
    S = 'atcoder'
    #output
    print(S[L-1:R])

if __name__ == '__main__':
    main()