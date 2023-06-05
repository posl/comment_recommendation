def main():
    n, m, q = map(int, input().split())
    wv = [list(map(int, input().split())) for _ in range(n)]
    x = list(map(int, input().split()))
    query = [list(map(int, input().split())) for _ in range(q)]
    for l, r in query:
        box = x[:l-1] + x[r:]
        box.sort()
        ans = 0
        for i in range(n):
            for j in range(len(box)):
                if wv[i][0] <= box[j]:
                    ans += wv[i][1]
                    box.pop(j)
                    break
        print(ans)
main()
