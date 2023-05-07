def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 最大値を求める
    maxA = max(A)
    # 素数リスト
    prime = []
    # 素数判定
    for i in range(2, maxA+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime.append(i)
    # 素因数分解
    prime_factor = []
    for i in range(N):
        prime_factor.append([])
        for j in prime:
            if A[i] % j == 0:
                prime_factor[i].append(j)
                while A[i] % j == 0:
                    A[i] = A[i] // j
    # 素因数の種類を求める
    count = 0
    for i in prime_factor:
        if len(i) == 1:
            count += 1
    print(count)
