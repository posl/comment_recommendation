def solve():
    # === 数値の入力 ===
    #n = int(input())
    #n, k = map(int, input().split())
    #a = list(map(int, input().split()))
    # === 行列の入力 ===
    #a = [list(map(int, input().split())) for _ in range(n)]
    S = input()
    if S[0] == S[1] == S[2] == S[3]:
        print('Bad')
    elif S[1] == S[2] == S[3]:
        print('Bad')
    elif S[0] == S[1] == S[2]:
        print('Bad')
    else:
        print('Good')
    return

if __name__ == '__main__':
    solve()