def main():
    n, q = map(int, input().split())
    L = []
    for i in range(n):
        L.append(list(map(int, input().split())))
    for i in range(q):
        s, t = map(int, input().split())
        print(L[s-1][t-1])
