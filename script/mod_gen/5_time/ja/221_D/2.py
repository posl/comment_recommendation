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
    #print("-----------")
    # 1日から10**9日までのリストを作る
    days = [0]*(10**9+1)
    #print(days)
    #print("-----------")
    # A[i]日目からB[i]日間連続でログインしているところを1とする
    for i in range(N):
        days[A[i]-1] += 1
        if A[i]+B[i] <= 10**9:
            days[A[i]+B[i]] -= 1
    #print(days)
    #print("-----------")
    # 1日目から10**9日目までのリストの累積和を取る
    for i in range(10**9):
        days[i+1] += days[i]
    #print(days)
    #print("-----------")
    # 1日目から10**9日目までのリストの各要素について、
    # ちょうどi人がログインしていた日数を出力する
    for i in range(1, N+1):
        ans = 0
        for j in range(10**9):
            if days[j] == i:
                ans += 1
        print(ans)

if __name__ == '__main__':
    main()