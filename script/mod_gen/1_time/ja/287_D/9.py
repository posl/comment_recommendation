def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        S_ = S[i:-(len(T)-i)]
        if S_.count('?') == len(T):
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()