def main():
    #read input
    S = input()
    T = input()
    #check if S is a prefix of T
    if T.startswith(S):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()