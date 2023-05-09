def main():
    #input
    Ps = list(map(int, input().split()))
    #compute
    S = ''
    for i in range(26):
        S += chr(ord('a')+Ps[i]-1)
    #output
    print(S)

if __name__ == '__main__':
    main()