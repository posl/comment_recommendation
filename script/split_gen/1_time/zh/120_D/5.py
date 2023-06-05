def main():
    n,m = map(int,input().split())
    bridges = []
    for i in range(m):
        bridges.append(list(map(int,input().split())))
    print(n,m)
    print(bridges)
