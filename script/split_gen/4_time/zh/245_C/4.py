def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    min_a = min(a)
    min_b = min(b)
    max_a = max(a)
    max_b = max(b)
    if max_a - min_a > k or max_b - min_b > k:
        print("No")
        return
    for i in range(n):
        if a[i] > b[i]:
            print("No")
            return
    print("Yes")
    return
