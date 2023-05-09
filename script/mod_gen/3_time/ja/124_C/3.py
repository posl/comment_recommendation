def main():
    S = input()
    prev = S[0]
    ans = 0
    for i in range(1, len(S)):
        if prev == S[i]:
            ans += 1
        else:
            prev = S[i]
    print(ans)

if __name__ == '__main__':
    main()