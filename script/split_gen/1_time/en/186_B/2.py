def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    A_sum = sum(sum(a) for a in A)
    A_min = min(min(a) for a in A)
    print(A_sum - H * W * A_min)
