def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    min_A = min([min(A[i]) for i in range(H)])
    print(sum([sum(A[i]) - min_A * W for i in range(H)]))
