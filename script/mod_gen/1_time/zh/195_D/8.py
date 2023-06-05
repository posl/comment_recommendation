def solve():
    N, M, Q = map(int, input().split())
    wv = [[int(i) for i in input().split()] for _ in range(N)]
    x = [int(i) for i in input().split()]
    query = [[int(i) for i in input().split()] for _ in range(Q)]
    wv.sort(key=lambda x: x[1], reverse=True)
    x.sort()
    for ql, qr in query:
        box = x[:ql-1] + x[qr:]
        box.sort()
        ans = 0
        for w, v in wv:
            for i in range(len(box)):
                if w <= box[i]:
                    ans += v
                    del box[i]
                    break
        print(ans)

if __name__ == '__main__':
    solve()