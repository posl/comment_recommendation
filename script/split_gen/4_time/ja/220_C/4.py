def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    sumA = sum(A)
    k = X // sumA
    X -= sumA * k
    cnt = k * N
    for a in A:
        X -= a
        cnt += 1
        if X < 0:
            break
    print(cnt)
