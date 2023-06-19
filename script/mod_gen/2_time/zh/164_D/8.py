def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        for j in range(i+3, len(S)+1):
            if int(S[i:j]) % 2019 == 0:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()