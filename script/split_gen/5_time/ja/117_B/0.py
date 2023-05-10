def main():
    # N = 4
    # L = [3, 8, 5, 1]
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    # print(N)
    # print(L)
    # 一番長い辺が他の N-1 辺の長さの合計よりも真に短い場合
    if L[-1] < sum(L[:-1]):
        print("Yes")
    else:
        print("No")
