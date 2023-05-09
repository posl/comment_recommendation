def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    for a in A:
        N -= a
        if N < 0:
            print(-1)
            return
    print(N)
