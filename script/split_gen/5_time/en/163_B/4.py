def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    sum_A = sum(A)
    if sum_A > N:
        print(-1)
    else:
        print(N-sum_A)
