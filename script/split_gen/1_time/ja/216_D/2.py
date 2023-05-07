def main():
    N, M = map(int, input().split())
    A = []
    for _ in range(M):
        k = int(input())
        A.append(list(map(int, input().split())))
    print('Yes' if solve(N, M, A) else 'No')
