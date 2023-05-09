def main():
    N, X = map(int, input().split())
    a, b = [], []
    for i in range(N):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    ans = 'No'
    for i in range(N):
        if X >= a[i] and X <= b[i]:
            ans = 'Yes'
    print(ans)
