def main():
    S = input()
    Q = S.count('?')
    MOD = 10**9 + 7
    ABC = 0
    # 3^Q 通りの文字列を作る
    for i in range(3**Q):
        # 3進数表現
        s = ''
        for j in range(Q):
            s += 'ABC'[(i // 3**j) % 3]
        # S の ? を置き換える
        j = 0
        for c in S:
            if c == '?':
                s = s[:j] + s[j+1:]
            j += 1
        # ABC の数を数える
        for j in range(len(s)):
            if s[j:j+3] == 'ABC':
                ABC += 1
    print(ABC % MOD)

if __name__ == '__main__':
    main()