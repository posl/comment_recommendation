def main():
    N = int(input())
    #都市間の道路情報を格納する辞書
    road = {}
    #都市1につながる道路を格納するリスト
    road[1] = []
    #都市1につながる道路の情報を格納する
    for i in range(N-1):
        A,B = map(int,input().split())
        if A == 1:
            road[1].append(B)
        if B == 1:
            road[1].append(A)
        road[A] = []
        road[B] = []
    #都市1につながる道路の情報を格納する
    for i in range(N-1):
        A,B = map(int,input().split())
        if A == 1:
            road[1].append(B)
        if B == 1:
            road[1].append(A)
        road[A].append(B)
        road[B].append(A)
    #都市1につながる道路をソートする
    road[1].sort()
    #都市1につながる道路の情報を格納する
    for i in range(N-1):
        A,B = map(int,input().split())
        if A == 1:
            road[1].append(B)
        if B == 1:
            road[1].append(A)
        road[A].append(B)
        road[B].append(A)
    #都市1につながる道路をソートする
    road[1].sort()
    #都市1につながる道路の情報を格納する
    for i in range(N-1):
        A,B = map(int,input().split())
        if A == 1:
            road[1].append(B)
        if B == 1:
            road[1].append(A)
        road[A].append(B)
        road[B].append(A)
    #都市1につながる道路をソートする
    road[1].sort()
    #都市1につながる道路の情報を格納する
    for i in range(N-1):
        A
