def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    A.sort()
    max = A[-1]
    is_div = [0] * (max + 1)
    for i in range(N):
        is_div[A[i]] = 1
    for i in range(1, max+1):
        if is_div[i] == 0:
            continue
        for j in range(2*i, max+1, i):
            is_div[j] = 0
    print(sum(is_div))
