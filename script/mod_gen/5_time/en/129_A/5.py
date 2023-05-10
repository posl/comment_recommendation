def main():
    #input
    P,Q,R = map(int,input().split())
    #compute
    result = P+Q+R-max(P,Q,R)
    #output
    print(result)

if __name__ == '__main__':
    main()