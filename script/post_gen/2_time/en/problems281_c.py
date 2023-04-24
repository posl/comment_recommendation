Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    t = T % total
    for i in range(N):
        if t < A[i]:
            print(i+1)
            print(t)
            break
        else:
            t -= A[i]

=======
Suggestion 2

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    S = sum(A)
    x = T % S
    for i in range(N):
        x -= A[i]
        if x <= 0:
            print(i + 1, A[i] + x)
            break

main()

=======
Suggestion 3

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    mod_T = T % sum_A
    if mod_T == 0:
        print(N, A[-1])
    else:
        for i in range(N):
            if mod_T - A[i] <= 0:
                print(i + 1, mod_T)
                break
            else:
                mod_T -= A[i]

=======
Suggestion 4

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    A_sum = sum(A)
    T = T % A_sum
    for i in range(N):
        T -= A[i]
        if T < 0:
            print(i + 1, A[i] + T)
            break

=======
Suggestion 5

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    t = 0
    for i in range(N):
        if t <= T and T <= t + A[i]:
            print(i + 1, T - t)
            return
        else:
            t += A[i]
    T = T % t
    for i in range(N):
        if t <= T and T <= t + A[i]:
            print(i + 1, T - t)
            return
        else:
            t += A[i]

=======
Suggestion 6

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0]
    for i in range(n):
        b.append(b[i] + a[i])
    for i in range(n):
        if b[i] <= t <= b[i + 1]:
            print(i + 1, t - b[i])
            break

=======
Suggestion 7

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, T)
    #print(A)
    sum = 0
    for i in range(N):
        sum += A[i]
        #print("sum", sum)
        if T <= sum:
            print(i+1, T-(sum-A[i]))
            break

=======
Suggestion 8

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(0)
    sum = 0
    for i in range(N):
        sum += A[i]
        if sum >= T:
            print(i+1, T - sum + A[i])
            break

=======
Suggestion 9

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, T)
    #print(A)
    #print(sum(A))
    #print(T % sum(A))
    #print(T // sum(A))
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    #print(A[6])
    #print(A[7])
    #print(A[8])
    #print(A[9])
    #print(A[10])
    #print(A[11])
    #print(A[12])
    #print(A[13])
    #print(A[14])
    #print(A[15])
    #print(A[16])
    #print(A[17])
    #print(A[18])
    #print(A[19])
    #print(A[20])
    #print(A[21])
    #print(A[22])
    #print(A[23])
    #print(A[24])
    #print(A[25])
    #print(A[26])
    #print(A[27])
    #print(A[28])
    #print(A[29])
    #print(A[30])
    #print(A[31])
    #print(A[32])
    #print(A[33])
    #print(A[34])
    #print(A[35])
    #print(A[36])
    #print(A[37])
    #print(A[38])
    #print(A[39])
    #print(A[40])
    #print(A[41])
    #print(A[42])
    #print(A[43])
    #print(A[44])
    #print(A[45])
    #print(A[46])
    #print(A[47])
    #print(A[48])
    #print(A[49])
    #print(A[50])
    #print(A[51])
    #print(A[52])
    #print(A[53])
    #print(A[54])
    #print(A[55])
    #print(A[56])
    #print(A[57])
    #print(A[58])
    #print(A[59])
    #print(A[60])
    #print(A[61])
    #print(A[62])

=======
Suggestion 10

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))

    # 1. 総再生時間を求める
    total_time = 0
    for i in range(N):
        total_time += A[i]

    # 2. Tを総再生時間で割った余りを求める
    T = T % total_time

    # 3. 余りを再生時間の合計から引く
    for i in range(N):
        T -= A[i]

        # 4. 余りがマイナスになったら、その時の曲番号を出力する
        if T < 0:
            print(i + 1, A[i] + T)
            break
