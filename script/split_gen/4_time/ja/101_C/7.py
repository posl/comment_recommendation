def main():
    N,K = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N-K):
        if A[i] != A[i+K]:
            count += 1
    print(count)
