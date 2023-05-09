def main():
    R, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(2)]
    print(A[1-R][C-1])
