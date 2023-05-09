def solve():
    # === 数値を取得 ===
    # N = int(input())
    S = input()
    # === 文字列を取得 ===
    # S = input()
    # === 処理 ===
    for i in range(0, len(S), 2):
        if S[i] not in ['R', 'U', 'D']:
            print('No')
            return
    for i in range(1, len(S), 2):
        if S[i] not in ['L', 'U', 'D']:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    solve()