def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if sum(A) > N:
        print(-1)
    else:
        print(N - sum(A))
