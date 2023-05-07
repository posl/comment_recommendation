def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    # N = 10**5
    # A = [1]*N
    # B = [1]*N
    # C = [1]*N
    # Bの値ごとのインデックスを取得
    B_idx = [[] for _ in range(N)]
    for i, b in enumerate(B):
        B_idx[b-1].append(i)
    # AとCの値が一致するときのBのインデックスの組み合わせを取得
    ans = 0
    for a in A:
        ans += len(B_idx[C[a-1]-1])
    print(ans)

if __name__ == '__main__':
    main()