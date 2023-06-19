def main():
    N, M = map(int, input().split())
    k = []
    s = []
    p = []
    for i in range(M):
        k.append(list(map(int, input().split())))
    for i in range(M):
        p.append(int(input()))
    print(N, M)
    print(k)
    print(p)
