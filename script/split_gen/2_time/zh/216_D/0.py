def main():
    N, M = map(int, input().split())
    k = []
    a = []
    for i in range(M):
        k.append(int(input()))
        a.append(list(map(int, input().split())))
    print(N, M, k, a)
    print("Yes" if N == 2 else "No")
