Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    k = int(input())
    h = 21
    m = 0
    m += k
    if m >= 60:
        h += 1
        m -= 60
    if h >= 24:
        h -= 24
    print(f"{h:02}:{m:02}")

=======
Suggestion 2

def main():
    k = int(input())
    h = 21 + k // 60
    m = k % 60
    print(str(h) + ":" + str(m).zfill(2))

=======
Suggestion 3

def main():
    #入力
    K = int(input())
    #計算
    HH = 21 + K // 60
    MM = K % 60
    #出力
    print(str(HH) + ":" + str(MM).zfill(2))

=======
Suggestion 4

def main():
    k = int(input())
    if k < 60:
        print("21:{}".format(k))
    else:
        print("22:{}".format(k - 60))

=======
Suggestion 5

def main():
    K = int(input())
    print('{0:02}:{1:02}'.format((21+K//60)%24,K%60))

=======
Suggestion 6

def main():
    #入力
    K = int(input())
    #初期化
    H = 21
    M = 0
    #計算
    M += K
    if M > 59:
        H += M // 60
        M = M % 60
    if H > 23:
        H = H % 24
    #出力
    print(str(H) + ":" + str(M).zfill(2))

=======
Suggestion 7

def main():
    #input
    K = int(input())

    #output
    print(str((21+K//60)%24)+":"+str(K%60).zfill(2))

=======
Suggestion 8

def main():
    K = int(input())
    #K = 63
    #K = 45
    #K = 100
    #21時ちょうどを基準にする
    HH = 21
    MM = 0
    #K分後の時間を計算する
    MM += K
    #MMが60以上になったら、HHを1増やし、MMを60から引く
    while MM >= 60:
        HH += 1
        MM -= 60
    #HHが24以上になったら、HHを24から引く
    while HH >= 24:
        HH -= 24
    #HHが1桁の場合、先頭に0を付ける
    if HH < 10:
        HH = "0" + str(HH)
    #MMが1桁の場合、先頭に0を付ける
    if MM < 10:
        MM = "0" + str(MM)
    print(str(HH) + ":" + str(MM))

=======
Suggestion 9

def main():
    k = int(input())
    print("21:{0:02d}".format((k+21)%60))

=======
Suggestion 10

def main():
    K = int(input())
    print("21:00")
    print("21:{}".format(K))
    print("21:%02d" % K)
    pri
