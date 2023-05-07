def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    p = [(0, 0)]
    for a in A:
        p.append((p[-1][0] + a, 0))
    p.append((x, y))
    for i in range(N):
        if p[i][0] == p[i+1][0] and p[i+1][0] == p[i+2][0]:
            if p[i][1] <= p[i+1][1] <= p[i+2][1] or p[i][1] >= p[i+1][1] >= p[i+2][1]:
                print("No")
                exit()
        elif p[i][1] == p[i+1][1] and p[i+1][1] == p[i+2][1]:
            if p[i][0] <= p[i+1][0] <= p[i+2][0] or p[i][0] >= p[i+1][0] >= p[i+2][0]:
                print("No")
                exit()
    print("Yes")
