def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    # Aの各要素の値をキーにして、出現回数を値にした辞書を作成
    D = {}
    for i in range(N):
        if A[i] not in D:
            D[A[i]] = 1
        else:
            D[A[i]] += 1
    # Cの各要素の値をキーにして、出現回数を値にした辞書を作成
    E = {}
    for i in range(N):
        if C[i] not in E:
            E[C[i]] = 1
        else:
            E[C[i]] += 1
    # Aの要素とCの要素のペアで、Aの要素がキーになっている辞書の値と、Cの要素がキーになっている辞書の値の積を求める
    ans = 0
    for i in range(N):
        if B[i] in D and C[i] in E:
            ans += D[B[i]] * E[C[i]]
    print(ans)
