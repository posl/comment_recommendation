def main():
    N, K = map(int, input().split())
    d = [0] * K
    A = [0] * K
    for i in range(K):
        d[i] = int(input())
        A[i] = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if (i + 1) not in A[0]:
            count += 1
    print(count)
