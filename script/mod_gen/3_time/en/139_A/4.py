def main():
    #input
    S = input()
    T = input()
    #compute
    ans = 0
    for i in range(3):
        if S[i] == T[i]:
            ans += 1
    #output
    print(ans)

if __name__ == '__main__':
    main()