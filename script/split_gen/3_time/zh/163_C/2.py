def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = [0] * N
    for i in range(N - 1):
        count[A[i] - 1] += 1
    for j in range(N):
        print(count[j])
