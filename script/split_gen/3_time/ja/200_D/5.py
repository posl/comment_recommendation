def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 200で割った余りの数列を作成
    A = [a % 200 for a in A]
    # 余りの数列を200個のリストに分類
    # 余りの数列を200個のリストに分類
    A = [list() for i in range(200)]
    for i, a in enumerate(A):
        A[a].append(i)
    # 余りの数列を200個のリストに分類
    for i in range(200):
        if len(A[i]) >= 2:
            print("Yes")
            print(len(A[i]), *A[i])
            print(len(A[i]), *A[i])
            return
    print("No")
