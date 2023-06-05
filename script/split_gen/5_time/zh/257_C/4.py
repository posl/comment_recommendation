def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    min_weight = 1
    max_weight = 10 ** 9
    while max_weight - min_weight > 1:
        mid = (max_weight + min_weight) // 2
        if is_ok(mid, N, S, W):
            min_weight = mid
        else:
            max_weight = mid
    print(min_weight)
