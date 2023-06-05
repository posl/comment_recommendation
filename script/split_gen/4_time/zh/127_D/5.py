def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    bc = [list(map(int, input().split())) for _ in range(m)]
    a.sort()
    bc.sort(key=lambda x: x[1], reverse=True)
    idx = 0
    for i in range(m):
        for j in range(bc[i][0]):
            if idx < n and a[idx] < bc[i][1]:
                a[idx] = bc[i][1]
                idx += 1
            else:
                break
    print(sum(a))
