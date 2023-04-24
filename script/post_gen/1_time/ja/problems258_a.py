Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    k = int(input())
    h = 21
    m = k
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
    h = 21
    m = k
    if m >= 60:
        h = h + m // 60
        m = m % 60
    if h >= 24:
        h = h % 24
    print('{0:02d}:{1:02d}'.format(h, m))

=======
Suggestion 3

def main():
    k = int(input())
    hh = 21
    mm = 0
    mm += k
    if mm >= 60:
        hh += 1
        mm -= 60
    if hh >= 24:
        hh -= 24
    print("{:02d}:{:02d}".format(hh, mm))

=======
Suggestion 4

def main():
    # 入力
    K = int(input())
    # 処理
    HH = (21 + K // 60) % 24
    MM = K % 60
    # 出力
    print(f"{HH:02}:{MM:02}")

=======
Suggestion 5

def main():
    k = int(input())
    print("{0:02d}:{1:02d}".format((21 + (k // 60)) % 24, (k % 60)))

=======
Suggestion 6

def main():
    #入力
    K = int(input())
    #時刻を計算
    HH = 21 + K // 60
    MM = K % 60
    #出力
    print(str(HH) + ":" + str(MM))

=======
Suggestion 7

def main():
    k = int(input())
    hour = 21
    minute = 0
    hour = (k + hour) % 24
    minute = k % 60
    print(str(hour).zfill(2) + ':' + str(minute).zfill(2))

=======
Suggestion 8

def main():
    #入力
    K = int(input())
    #計算
    #HH = 21 + K // 60
    #MM = K % 60
    HH, MM = divmod(21*60 + K, 60)
    #出力
    print("{:02}:{:02}".format(HH, MM))

=======
Suggestion 9

def main():
    K = int(input())
    #21時ちょうどからの経過時間
    time = 21 * 60 + K
    #24時間制の時間
    hour = time // 60
    #分
    minute = time % 60
    print("{0:02}:{1:02}".format(hour, minute))

=======
Suggestion 10

def main():
    #入力
    K = int(input())

    #処理
    #21時からK分後の時刻を求める
    #HH:MMの形式で出力
    #HHは24時間制での時間を、MMは分を表す
    #時間または分が1桁のときは、先頭に0を追加して2桁の整数として表す
    #HH = 21 + K // 60
    #MM = (K % 60)
    HH = 21 + (K // 60)
    MM = (K % 60)
    if HH >= 24:
        HH = HH - 24
    if HH < 10:
        HH = '0' + str(HH)
    if MM < 10:
        MM = '0' + str(MM)
    print(str(HH) + ':' + str(MM))
