def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = [0] * (N+1)
    for i in range(N):
        count[A[i]] += 1
    for i in range(N):
        print(N-1-count[A[i]])
