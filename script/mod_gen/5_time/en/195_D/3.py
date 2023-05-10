def solve():
    n, m, q = map(int, input().split())
    wv = [tuple(map(int, input().split())) for _ in range(n)]
    x = list(map(int, input().split()))
    query = [tuple(map(int, input().split())) for _ in range(q)]
    wv.sort(key=lambda x: -x[1])
    x = sorted([(i, j) for i, j in enumerate(x)], key=lambda x: x[1])
    for l, r in query:
        box = x[:l-1] + x[r:]
        box.sort(key=lambda x: x[0])
        ans = 0
        for i, j in wv:
            for k in range(len(box)):
                if box[k][1] >= i:
                    box.pop(k)
                    break
            else:
                continue
            ans += j
        print(ans)

if __name__ == '__main__':
    solve()