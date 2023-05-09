def main():
    S = input()
    L = len(S)
    ans = 0
    for i in range(L):
        for j in range(i+4,L):
            if int(S[i:j+1])%2019 == 0:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()