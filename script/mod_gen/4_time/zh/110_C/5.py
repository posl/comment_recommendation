def main():
    S = input()
    T = input()
    dic = {}
    for i in range(len(S)):
        if S[i] in dic:
            if dic[S[i]] != T[i]:
                print("No")
                return
        dic[S[i]] = T[i]
    print("Yes")

if __name__ == '__main__':
    main()