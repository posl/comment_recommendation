def main():
    # 入力
    N, M = map(int, input().split())
    A = [0] * N
    for i in range(N):
        A[i] = list(map(int, input().split()))
        A[i].pop(0)
    # 処理
    ans = 0
    for i in range(1, M+1):
        flag = True
        for j in range(N):
            if i not in A[j]:
                flag = False
        if flag:
            ans += 1
    # 出力
    print(ans)
