def main():
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    result = "No"
    for i in range(N):
        if a[i] <= X <= b[i]:
            result = "Yes"
            break
    print(result)
