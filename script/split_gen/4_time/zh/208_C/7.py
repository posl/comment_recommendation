def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    n = K // N
    k = K % N
    for i in range(N):
        if i < k:
            print(n+1)
        else:
            print(n)
