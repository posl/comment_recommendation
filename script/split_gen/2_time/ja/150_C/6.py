def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    # 順列を列挙
    from itertools import permutations
    perms = permutations(range(1, N+1))
    # 辞書順でソート
    perms = sorted(perms)
    # 何番目かを調べる
    print(abs(perms.index(tuple(P)) - perms.index(tuple(Q))))
