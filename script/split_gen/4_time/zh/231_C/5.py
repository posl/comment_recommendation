def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    x = []
    for i in range(Q):
        x.append(int(input()))
    A.sort()
    for i in range(Q):
        count = 0
        for j in range(N):
            if A[j] >= x[i]:
                count += 1
        print(count)
    return 0
