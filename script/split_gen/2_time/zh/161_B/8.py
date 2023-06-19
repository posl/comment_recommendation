def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    total = sum(a)
    threshold = total / (4 * m)
    if a[m - 1] >= threshold:
        print("是")
    else:
        print("否")
