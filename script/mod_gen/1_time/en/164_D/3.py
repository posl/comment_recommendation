def main():
    S = input()
    L = len(S)
    ans = 0
    for i in range(L):
        for j in range(i+1,L+1):
            if int(S[i:j]) % 2019 == 0:
                ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()