def main():
    #input
    N = int(input())
    S = input()
    #output
    if S[:N//2] == S[N//2:]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()