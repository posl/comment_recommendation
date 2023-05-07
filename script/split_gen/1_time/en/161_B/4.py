def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if A[-M] >= sum(A) / (4 * M):
        print('Yes')
    else:
        print('No')
