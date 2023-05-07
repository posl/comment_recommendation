def main():
    S = input()
    ans = ""
    for i in range(len(S)):
        if i == len(S) - 1:
            ans += "0"
        else:
            ans += S[i + 1]
    print(ans)

if __name__ == '__main__':
    main()