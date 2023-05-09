def main():
    import sys
    from itertools import permutations
    N, M = map(int, sys.stdin.readline().split())
    S = [sys.stdin.readline().rstrip() for _ in range(N)]
    T = [sys.stdin.readline().rstrip() for _ in range(M)]
    for p in permutations(S):
        for i in range(1, 2**N):
            # 組み合わせの数は2**N-1なので、2**N-1から1ずつ減らしていく
            # 2進数に変換したときの桁が1であるところを_とする
            # 例えば、i=4のとき、4の2進数は100なので、S[0]とS[2]の間に_を入れる
            X = p[0]
            for j in range(1, N):
                if (i >> j) & 1:
                    X += '_' + p[j]
                else:
                    X += p[j]
            if 3 <= len(X) <= 16 and X not in T:
                print(X)
                return
    print(-1)

if __name__ == '__main__':
    main()