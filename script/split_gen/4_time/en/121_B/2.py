def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    count = 0
    for i in range(N):
        A = list(map(int, input().split()))
        if sum([A[j]*B[j] for j in range(M)]) + C > 0:
            count += 1
    print(count)