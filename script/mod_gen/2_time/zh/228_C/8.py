def main():
    n, k = map(int, input().split())
    p = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        p[i].sort(reverse=True)
        p[i].append(sum(p[i]))
        p[i].append(i)
    p.sort(reverse=True)
    p.append([0, 0, 0, 0, 0])
    rank = 1
    for i in range(n):
        if p[i][3:] != p[i + 1][3:]:
            rank = i + 1
        if rank <= k:
            print("Yes")
        else:
            print("No")
main()
