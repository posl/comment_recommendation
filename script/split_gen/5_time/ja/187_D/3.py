def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    # 青木氏の票の合計
    aoki = sum(A)
    #print(aoki)
    # 高橋氏の票の合計
    takahashi = 0
    for i in range(N):
        takahashi += B[i] * 2
    #print(takahashi)
    # 各町の高橋氏の票の差分
    diff = []
    for i in range(N):
        diff.append(A[i] + B[i] * 2)
    #print(diff)
    diff.sort(reverse=True)
    #print(diff)
    count = 0
    for i in range(N):
        if takahashi <= aoki:
            break
        takahashi -= diff[i]
        count += 1
    print(count)
