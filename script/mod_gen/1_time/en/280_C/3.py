def main():
    S = input()
    T = input()
    for i in range(len(S)):
        if S[i] != T[i]:
            print(i+1)
            return
    print(len(S)+1)

if __name__ == '__main__':
    main()