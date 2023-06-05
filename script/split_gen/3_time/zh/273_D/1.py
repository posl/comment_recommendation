def main():
    H, W, rs, cs = map(int, input().split())
    N = int(input())
    r = [0] * N
    c = [0] * N
    for i in range(N):
        r[i], c[i] = map(int, input().split())
    Q = int(input())
    d = [0] * Q
    l = [0] * Q
    for i in range(Q):
        d[i], l[i] = input().split()
        l[i] = int(l[i])
    #print(H, W, rs, cs)
    #print(N)
    #print(r)
    #print(c)
    #print(Q)
    #print(d)
    #print(l)
    # 1. 求出每个方块的左、右、上、下的邻接方块
    # 2. 求出每个方块的左、右、上、下的邻接方块中没有墙的方块
    # 3. 求出每个方块的左、右、上、下的邻接方块中没有墙的方块中的最小的方块
    # 4. 求出每个方块的左、右、上、下的邻接方块中没有墙的方块中的最小的方块的位置
    # 5. 求出每个方块的左、右、上、下的邻接方块中没有墙的方块中的最小的方块的位置的位置
    # 6. 求出每个方块的左、右、上、下的邻接方块中没有墙的方块中的最小的方块的位置的位置的方块
    # 7. 求出每个方块的左、右、上、下的邻接方块中没有墙的方块中的最小的方块的位置的位置的方块的位置
    # 8. 求出每个方块的左、右、上、
