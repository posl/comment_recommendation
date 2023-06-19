def main():
    S = input()
    T = input()
    # print(S)
    # print(T)
    for i in range(len(S)):
        if S[0:i] + S[i+1:] == T:
            print(i+1)
            break
    else:
        print(len(S)+1)

if __name__ == '__main__':
    main()