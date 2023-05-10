def main():
    S = input()
    N = len(S)
    #print(N)
    #print(S)
    count = 0
    #print(S[1])
    for i in range(0,N-1):
        #print(S[i])
        #print(S[i+1])
        if S[i] != S[i+1]:
            count += 1
    print(count)
main()

if __name__ == '__main__':
    main()