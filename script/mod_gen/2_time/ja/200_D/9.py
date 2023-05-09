def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 200
    # 余りをキーに、その余りを持つ要素のインデックスをリストで保持する
    r2idxs = [[] for _ in range(mod)]
    for i, a in enumerate(A):
        r2idxs[a % mod].append(i + 1)
    for r in range(mod):
        if len(r2idxs[r]) >= 2:
            print("Yes")
            print(len(r2idxs[r]), *r2idxs[r])
            print(len(r2idxs[r]), *r2idxs[r])
            return
    print("No")

if __name__ == '__main__':
    main()