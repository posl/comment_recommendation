def main():
    N = int(input())
    s = [input() for _ in range(N)]
    # sの文字列をソートして、辞書型にして、valueが2以上のものを数える
    ans = 0
    for i in range(N):
        s_dict = {}
        for j in range(N):
            if i != j:
                s_dict["".join(sorted(s[i]))] = s_dict.get("".join(sorted(s[i])), 0) + 1
        for v in s_dict.values():
            if v >= 2:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()