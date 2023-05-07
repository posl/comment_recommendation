def main():
    n = int(input())
    w = [int(i) for i in input().split()]
    min_diff = 10000
    for i in range(1, n):
        s1 = sum(w[:i])
        s2 = sum(w[i:])
        diff = abs(s1 - s2)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)
