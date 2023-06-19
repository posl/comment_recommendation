def main():
    S = input()
    T = input()
    for i in range(0,len(S)):
        if S[i] != T[i]:
            print(i+1)
            break
    else:
        print(len(S)+1)

if __name__ == '__main__':
    main()