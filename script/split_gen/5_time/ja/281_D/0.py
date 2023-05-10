def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    count = 0
    for i in range(K):
        count += A[i]
    if count == 0:
        print(0)
        return
    if count % D != 0:
        print(count)
        return
    if count // D == 1:
        print(-1)
        return
    print(count - 1)
