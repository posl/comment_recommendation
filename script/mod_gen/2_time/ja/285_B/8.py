def main():
    N = int(input())
    S = input()
    for i in range(1, N):
        #print(S[:i])
        #print(S[i:])
        #print(set(S[:i]) & set(S[i:]))
        print(len(S[:i]) - len(set(S[:i]) & set(S[i:])))

if __name__ == '__main__':
    main()