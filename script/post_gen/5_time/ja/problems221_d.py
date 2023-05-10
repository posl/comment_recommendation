Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    #print("solve")
    #print("N:{}

=======
Suggestion 2

def main():
    n = int(input())
    login = [0] * (10**9 + 2)
    for _ in range(n):
        a, b = map(int, input().split())
        login[a] += 1
        login[a+b] -= 1
    for i in range(1, 10**9 + 2):
        login[i] += login[i-1]
    print(*login[1:-1])

=======
Suggestion 3

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

=======
Suggestion 4

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    max_a = max(a)
    max_b = max(b)
    if max_a + max_b > 10**9:
        max_day = 10**9
    else:
        max_day = max_a + max_b
    day = [0 for i in range(max_day + 1)]
    for i in range(n):
        for j in range(a[i], a[i] + b[i]):
            day[j] += 1
    for i in range(1, n + 1):
        print(day.count(i), end = " ")

=======
Suggestion 5

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

=======
Suggestion 6

def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    #print(N)
    #print(A)
    #print(B)

    # 1. 各プレイヤーがログインしていた日付を全て配列に入れる
    # 2. 日付をソートする
    # 3. 各日付について、その日付が何人ログインしていたかを数える
    # 4. 出力

    # 1. 各プレイヤーがログインしていた日付を全て配列に入れる
    dates = []
    for i in range(N):
        for j in range(B[i]):
            dates.append(A[i] + j)
    #print(dates)

    # 2. 日付をソートする
    dates.sort()
    #print(dates)

    # 3. 各日付について、その日付が何人ログインしていたかを数える
    #    その日付が何人ログインしていたかを数えるには、
    #    その日付より前にログインしていた人数を数える必要がある。
    #    そのため、日付ごとに、その日付より前にログインしていた人数を記録する配列を作る。
    #    その配列を作りながら、その日付が何人ログインしていたかを数える。
    #    その日付より前にログインしていた人数を記録する配列の初期値は0とする。
    #    その日付が何人ログインしていたかを数えるには、
    #    その日付が出現した回数を数える必要がある。
    #    そのため、日付ごとに、その日付が出現した回数を記録する配列を

=======
Suggestion 7

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    
    ans = [0] * (10**9+2)
    for i in range(n):
        ans[a[i]] += 1
        ans[a[i]+b[i]] -= 1
    
    for i in range(1, 10**9+2):
        ans[i] += ans[i-1]
    
    for i in range(1, n+1):
        print(ans[i], end=' ')

=======
Suggestion 8

def main():
    N = int(input())
    login = []
    for i in range(N):
        a, b = map(int, input().split())
        login.append([a, b])
    login.sort()
    max_day = 0
    for i in range(N):
        if login[i][0] + login[i][1] > max_day:
            max_day = login[i][0] + login[i][1]
    #print(max_day)
    login_day = [0] * (max_day + 1)
    for i in range(N):
        login_day[login[i][0]] += 1
        login_day[login[i][0] + login[i][1]] -= 1
    #print(login_day)
    for i in range(1, max_day + 1):
        login_day[i] += login_day[i - 1]
    for i in range(1, max_day + 1):
        print(login_day[i], end=" ")
    print()

=======
Suggestion 9

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
    #D = [0] * N
    D = [0 for i in range(N)]
    #print(D)
    for i in range(N):
        for j in range(A[i], A[i]+B[i]):
            if j <= N:
                D[j-1] += 1
    print(*D)

=======
Suggestion 10

def main():
    N = int(input())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i],B[i] = map(int,input().split())
    #print(N,A,B)
    #print(A[0],B[0])
    #print(A[1],B[1])
    #print(A[2],B[2])
    #print(A[3],B[3])
    #print(A[4],B[4])
    #print(A[5],B[5])
    #print(A[6],B[6])
    #print(A[7],B[7])
    #print(A[8],B[8])
    #print(A[9],B[9])
    #print(A[10],B[10])
    #print(A[11],B[11])
    #print(A[12],B[12])
    #print(A[13],B[13])
    #print(A[14],B[14])
    #print(A[15],B[15])
    #print(A[16],B[16])
    #print(A[17],B[17])
    #print(A[18],B[18])
    #print(A[19],B[19])
    #print(A[20],B[20])
    #print(A[21],B[21])
    #print(A[22],B[22])
    #print(A[23],B[23])
    #print(A[24],B[24])
    #print(A[25],B[25])
    #print(A[26],B[26])
    #print(A[27],B[27])
    #print(A[28],B[28])
    #print(A[29],B[29])
    #print(A[30],B[30])
    #print(A[31],B[31])
    #print(A[32],B[32])
    #print(A[33],B[33])
    #print(A[34],B[34])
    #print(A[35],B[35])
    #print(A[36],B[36])
    #print(A[37],B[37])
    #print(A[38],B[38])
    #print(A[39],B[39])
    #print(A[40],B
