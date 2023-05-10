def main():
    S = input()
    T = input()
    #print(S)
    #print(T)
    #print(len(S))
    #print(len(T))
    if len(S) + 1 != len(T):
        print('No')
        return
    if S == T[:-1]:
        print('Yes')
        return
    print('No')

if __name__ == '__main__':
    main()