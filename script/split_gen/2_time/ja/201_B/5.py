def main():
    N = int(input())
    d = {}
    for i in range(N):
        S, T = map(str, input().split())
        d[S] = int(T)
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    print(d[1][0])
