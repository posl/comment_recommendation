def isPolygon(L):
    L.sort(reverse=True)
    return L[0] < sum(L[1:])
N = int(input())
L = list(map(int, input().split()))
print("是" if isPolygon(L) else "否")
