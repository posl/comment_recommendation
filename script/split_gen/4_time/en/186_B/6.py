def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    A = [item for sublist in A for item in sublist]
    print(sum([abs(i - sum(A) / (H * W)) for i in A]) // 2)
