def main():
    n, k = map(int, input().split())
    if k % 2 == 0:
        count = n // k
        count = count ** 3
        count += (n // (k // 2) - count) ** 3
    else:
        count = n // k
        count = count ** 3
    print(count)
