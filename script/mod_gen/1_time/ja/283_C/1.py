def main():
    S = input()
    S = S[::-1]
    ans = 0
    for i in range(len(S)):
        if i == 0:
            ans += int(S[i]) + 1
        else:
            ans += int(S[i]) + 10
    print(ans)

if __name__ == '__main__':
    main()