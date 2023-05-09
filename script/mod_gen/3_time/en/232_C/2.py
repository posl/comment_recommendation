def solve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(M)]
    AB.sort()
    CD.sort()
    for i in range(M):
        AB[i].sort()
        CD[i].sort()
    AB.sort()
    CD.sort()
    for i in range(M):
        if AB[i] != CD[i]:
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    solve()