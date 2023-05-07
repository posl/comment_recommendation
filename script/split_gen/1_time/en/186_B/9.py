def main():
    # Read data
    H, W = map(int, input().split())
    A = [[int(a) for a in input().split()] for _ in range(H)]
    # Find minimum number of blocks
    min_ = min([min(a) for a in A])
    ans = 0
    for a in A:
        ans += sum([i - min_ for i in a])
    # Print answer
    print(ans)
