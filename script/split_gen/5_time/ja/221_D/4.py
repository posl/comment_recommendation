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
    #1日目から10^9日目までのログイン数をカウントする
    login_count = [0 for i in range(1000000000)]
    for i in range(N):
        for j in range(A[i], A[i]+B[i]):
            login_count[j] += 1
    #print(login_count)
    #ログイン数ごとに日数をカウントする
    answer = [0 for i in range(N)]
    for i in range(1000000000):
        if login_count[i] > 0:
            answer[login_count[i]-1] += 1
    #print(answer)
    #出力
    for i in range(N):
        print(answer[i], end=" ")
    print()
