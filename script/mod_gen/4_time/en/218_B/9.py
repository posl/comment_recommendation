def main():
    #input
    P = list(map(int, input().split()))
    
    #compute
    S = [chr(97+i) for i in range(26)]
    for i in range(26):
        S[i],S[P[i]-1] = S[P[i]-1],S[i]
    
    #output
    print(''.join(S))

if __name__ == '__main__':
    main()