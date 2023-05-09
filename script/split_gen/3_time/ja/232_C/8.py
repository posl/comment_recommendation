def main():
    N, M = map(int, input().split())
    AB = []
    CD = []
    for i in range(M):
        a, b = map(int, input().split())
        AB.append((a, b))
    for i in range(M):
        c, d = map(int, input().split())
        CD.append((c, d))
    AB.sort()
    CD.sort()
    AB = tuple(AB)
    CD = tuple(CD)
    if AB == CD:
        print("Yes")
    else:
        print("No")
