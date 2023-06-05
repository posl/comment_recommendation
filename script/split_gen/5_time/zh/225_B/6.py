def main():
    n = int(input())
    nodes = {}
    for i in range(n-1):
        a,b = map(int,input().split())
        nodes[a] = nodes.get(a,0)+1
        nodes[b] = nodes.get(b,0)+1
    if max(nodes.values()) == n-1:
        print("Yes")
    else:
        print("No")
