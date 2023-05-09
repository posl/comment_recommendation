def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 2N+1の配列を用意
    ans = [0] * (2 * N + 1)
    # Aの要素を1から順に見ていく
    for i in range(N):
        # A[i]の親はA[i]の2倍-1を2で割ったもの
        parent = (A[i] * 2 - 1) // 2
        # A[i]の親はA[i]の2倍-1を2で割ったもの
        ans[A[i] * 2 - 1] = ans[parent] + 1
        # A[i]の親はA[i]の2倍を2で割ったもの
        ans[A[i] * 2] = ans[parent] + 1
    for i in range(2 * N + 1):
        print(ans[i])
