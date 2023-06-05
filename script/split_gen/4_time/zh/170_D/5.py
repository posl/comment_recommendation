def main():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    max_A = A[-1]
    cnt = 0
    check = [True] * (max_A + 1)
    for i in range(n):
        if check[A[i]]:
            cnt += 1
            for j in range(A[i], max_A + 1, A[i]):
                check[j] = False
    print(cnt)
