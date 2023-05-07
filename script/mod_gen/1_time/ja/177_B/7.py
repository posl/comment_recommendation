def main():
    S = input()
    T = input()
    S = list(S)
    T = list(T)
    S.reverse()
    T.reverse()
    ans = 0
    for i in range(len(T)):
        if S[i] != T[i]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()