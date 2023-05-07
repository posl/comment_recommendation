def main():
    #入力
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    #処理
    cnt = 0
    for i in range(N):
        if sum([a*b for a,b in zip(A[i],B)]) + C > 0:
            cnt += 1
    #出力
    print(cnt)
