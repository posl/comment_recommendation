def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    from collections import Counter
    counter = Counter(A)
    sumA = sum(A)
    for B, C in BC:
        sumA += (C - B) * counter[B]
        counter[C] += counter[B]
        counter[B] = 0
        print(sumA)
