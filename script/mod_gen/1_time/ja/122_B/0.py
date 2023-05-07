def main():
    S = input()
    ans = 0
    cnt = 0
    for i in range(len(S)):
        if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()