def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    total = 0
    for i in range(N):
        total += A[i]
    num = T // total
    mod = T % total
    if mod == 0:
        mod = total
        num -= 1
    total = 0
    for i in range(N):
        total += A[i]
        if total >= mod:
            print(i + 1, mod - (total - A[i]))
            break
