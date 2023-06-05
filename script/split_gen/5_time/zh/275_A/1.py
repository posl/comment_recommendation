def max_height_bridge():
    n = int(input())
    bridges = list(map(int, input().split()))
    max_height = max(bridges)
    print(bridges.index(max_height)+1)
