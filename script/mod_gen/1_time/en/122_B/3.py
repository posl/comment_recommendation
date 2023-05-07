def main():
    S = input()
    ans = 0
    cnt = 0
    for i in range(len(S)):
        if S[i] in "ACGT":
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()