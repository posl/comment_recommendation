def main():
    n,m = map(int,input().split())
    edge = [list(map(int,input().split())) for _ in range(m)]
    print(edge)
    print(n,m)
    print(edge[0][0])
