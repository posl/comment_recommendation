def main():
    N, M = map(int, input().split())
    K = []
    A = []
    for i in range(N):
        k, *a = map(int, input().split())
        K.append(k)
        A.append(a)
    count = 0
    for i in range(1, M + 1):
        for j in range(N):
            if i in A[j]:
                count += 1
        if count == N:
            break
        count = 0
    print(count)
