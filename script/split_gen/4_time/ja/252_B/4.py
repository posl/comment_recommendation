def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort()
    for i in range(K):
        if A[i] < B[i]:
            print("Yes")
            exit()
    print("No")
    return
