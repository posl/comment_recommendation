def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        if S[i] == '0':
            continue
        elif i == 0:
            ans += 1
        else:
            ans += 2
        ans += int(S[i])
    print(ans)

if __name__ == '__main__':
    main()