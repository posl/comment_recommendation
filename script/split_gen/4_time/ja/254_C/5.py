def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    B.sort()
    B.reverse()
    for i in range(K):
        if A[i] < B[i]:
            print("Yes")
            exit()
    print("No")
