def solve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(M)]
    AB.sort()
    CD.sort()
    for i in range(M):
        AB[i].append(i)
        CD[i].append(i)
    AB.sort(key=lambda x: x[1])
    CD.sort(key=lambda x: x[1])
    if AB == CD:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()