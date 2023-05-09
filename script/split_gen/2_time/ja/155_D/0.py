def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] >= 0:
        print(A[K-1] * A[K-2])
        return
    if A[-1] <= 0:
        print(A[-K] * A[-K-1])
        return
    # 0を境にして、0を含むほうが大きいほうを正とする
    if abs(A[0]) > abs(A[-1]):
        pos = 0
        neg = N
    else:
        pos = N
        neg = 0
    for i in range(N):
        if A[i] > 0:
            pos = i
            break
    for i in range(N-1, -1, -1):
        if A[i] < 0:
            neg = i+1
            break
    # print(pos, neg)
    # pos, negを境にして、K番目にくる数は、
    # 1. pos, negの積
    # 2. pos-1, negの積
    # 3. pos, neg+1の積
    # 4. pos-1, neg+1の積
    # のいずれかになる。
    # ただし、2, 3の場合は、pos-1, neg+1の積のほうが大きい場合がある。
    # それを考慮して、積の大きいほうを選ぶ。
    # ただし、pos-1, neg+1の積のほうが大きい場合は、
    # 1. pos, negの積
    # 2. pos-1, negの積
    # 3. pos, neg+1の積
    # のいずれかになる。
    # それを考慮して、積の大きいほうを選ぶ。
    # 1, 2の場合は、pos-1, negの積のほうが
