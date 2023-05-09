def main():
    n = int(input())
    weights = [int(i) for i in input().split()]
    min_diff = sum(weights)
    for t in range(1, n):
        s1 = sum(weights[:t])
        s2 = sum(weights[t:])
        diff = abs(s1 - s2)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)
