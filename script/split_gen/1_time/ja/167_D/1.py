def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, -1)
    ans = 1
    for i in range(K):
        ans = A[ans]
    print(ans)
