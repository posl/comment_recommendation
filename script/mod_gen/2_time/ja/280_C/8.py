def main():
    S = input()
    T = input()
    #print(S)
    #print(T)
    for i in range(len(S)+1):
        if S[:i] == T[:i] and S[i:] == T[i+1:]:
            print(i+1)
            break

if __name__ == '__main__':
    main()