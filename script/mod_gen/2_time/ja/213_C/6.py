def main():
    H, W, N = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # 重複を削除
    A = list(set(A))
    B = list(set(B))
    # ソート
    A.sort()
    B.sort()
    # 座標を圧縮
    A = {a: i + 1 for i, a in enumerate(A)}
    B = {b: i + 1 for i, b in enumerate(B)}
    for a, b in zip(A, B):
        print(A[a], B[b])

if __name__ == '__main__':
    main()