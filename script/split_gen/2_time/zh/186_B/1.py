def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
    min_a = min([min(a) for a in A])
    print(sum([sum(a) for a in A]) - min_a * H * W)
