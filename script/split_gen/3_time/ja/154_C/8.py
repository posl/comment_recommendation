def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    #ソート
    A.sort()
    #出力
    for i in range(N-1):
        if A[i] == A[i+1]:
            print('NO')
            return
    print('YES')
