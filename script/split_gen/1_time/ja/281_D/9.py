def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    
    # 配列Aの中で、A[i]を最小値として、A[i] + A[i+1] + ... + A[j] <= K*Dを満たす最大のjを求める
    # このとき、A[i] + A[i+1] + ... + A[j]は、A[i]を最小値とするK個の数の和になる
    # このK個の数をA[i]からA[j]までの数とすると、A[i] + A[i+1] + ... + A[j]は、A[i]を最小値とするK個の数の和になる
    # このK個の数をA[i]からA[j]までの数とすると、A[i] + A[i+1] + ... + A[j]は、A[i]を最小値とするK個の数の和になる
    # このK個の数をA[i]からA[j]までの数とすると、A[i] + A[i+1] + ... + A[j]は、A[i]を最小値とするK個の数の和になる
    # このK個の数をA[i]からA[j]までの数とすると、A[i] + A[i+1] + ... + A[j]は、A[i]を最小値とするK個の数の和になる
    # このK個の数をA[i]からA[j]までの数とすると、A[i] + A[i+1] + ... + A[j]は、A[i]を最小値とするK個の数の和になる
    # このK個の数をA[i]からA[j]までの数とすると、A[i] + A[i+1] + ... + A[j]は、A[i]を最小値とするK個