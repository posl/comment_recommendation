def main():
    S = str(input())
    cnt = 0
    for i in range(10000):
        s = str(i).zfill(4)
        for j in range(4):
            if S[int(s[j])] == "o" and S[int(s[j])] != s[j]:
                break
            if S[int(s[j])] == "x" and S[int(s[j])] == s[j]:
                break
        else:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()