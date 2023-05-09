def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print((N - 1) * N // 2 - (N - len(set(A))))
