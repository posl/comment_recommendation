def main():
    S = input()
    n = len(S)
    ans = 0
    for i in range(n):
        for j in range(i+3,n):
            if int(S[i:j+1]) % 2019 == 0:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()