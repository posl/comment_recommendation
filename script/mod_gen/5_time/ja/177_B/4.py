def main():
    s = input()
    t = input()
    slen = len(s)
    tlen = len(t)
    ans = tlen
    for i in range(slen-tlen+1):
        cnt = 0
        for j in range(tlen):
            if s[i+j] != t[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)
main()  # 出力結果 0.0sec

if __name__ == '__main__':
    main()