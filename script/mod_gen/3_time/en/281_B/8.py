def main():
    #input
    S = input()
    #compute
    if S[0].isupper() and S[-1].isupper() and len(S)==8 and S[1:7].isdigit() and 100000<=int(S[1:7])<=999999:
        print('Yes')
    else:
        print('No')
    #output

if __name__ == '__main__':
    main()