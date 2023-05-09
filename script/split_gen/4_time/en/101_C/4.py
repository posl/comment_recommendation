def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    while N > 1:
        N -= K - 1
        count += 1
    print(count)
    return
