def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a - 1 for a in A]
    #print(N, K)
    #print(A)
    # 1からスタート
    # K回テレポートする
    # K回目に到着する町を出力
    # 1からスタート
    # 1 -> A[0] -> A[A[0]] -> A[A[A[0]]] -> A[A[A[A[0]]]] -> ...
    # 1 -> A[0] -> A[A[0]] -> A[A[A[0]]] -> A[A[A[A[0]]]] -> ...
    # 1 -> A[0] -> A[A[0]] -> A[A[A[0]]] -> A[A[A[A[0]]]] -> ...
    # 1 -> A[0] -> A[A[0]] -> A[A[A[0]]] -> A[A[A[A[0]]]] -> ...
    # 1 -> A[0] -> A[A[0]] -> A[A[A[0]]] -> A[A[A[A[0]]]] -> ...
    # 1 -> A[0] -> A[A[0]] -> A[A[A[0]]] -> A[A[A[A[0]]]] -> ...
    # 1 -> A[0] -> A[A[0]] -> A[A[A[0]]] -> A[A[A[A[0]]]] -> ...
    # 1 -> A[0] -> A[A[0]] -> A[A[A[0]]] -> A[A[A[A[0]]]] -> ...
    # 1 -> A[0] -> A[A[0]] -> A[A[A[0]]] -> A[A[A[A[0]]]] -> ...
    # 1 -> A[0] -> A[A[0]] -> A[A[A[0]]] -> A[A[A[A[0]]]] -> ...
    # 1 -> A[0] -> A[A[0]] -> A[A[A[0]]] -> A[A[A[A[0]]]] -> ...
    # 1 -> A[0] -> A[A[0]] -> A[A[A[0]]] -> A[A[A[A[0]]]]

if __name__ == '__main__':
    main()