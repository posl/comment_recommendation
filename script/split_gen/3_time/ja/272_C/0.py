def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    for i in range(N):
        if A[i] % 2 == 0:
            print(A[i])
            return
    print(-1)
