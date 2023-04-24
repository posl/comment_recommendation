Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    from collections import deque
    K = int(input())
    q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
    for _ in range(K):
        n = q.popleft()
        q.append(n * 10 + n % 10 - 1)
        q.append(n * 10 + n % 10)
        q.append(n * 10 + n % 10 + 1)
    print(n)

=======
Suggestion 2

def main():
    k = int(input())
    q = [1,2,3,4,5,6,7,8,9]
    for i in range(k):
        x = q.pop(0)
        if x % 10 > 0:
            q.append(10*x + x%10 - 1)
        q.append(10*x + x%10)
        if x % 10 < 9:
            q.append(10*x + x%10 + 1)
    print(x)

=======
Suggestion 3

def main():
    #入力
    K = int(input())
    #ルンルン数を格納するリスト
    L = [1,2,3,4,5,6,7,8,9]
    #ルンルン数を格納するリストにルンルン数を追加していく
    for i in range(10**5):
        s = str(L[i])
        #ルンルン数の末尾の数字
        last = int(s[-1])
        #ルンルン数の末尾の数字が9の場合
        if last == 9:
            L.append(int(s+str(last-1)))
        #ルンルン数の末尾の数字が0の場合
        elif last == 0:
            L.append(int(s+str(last+1)))
        #ルンルン数の末尾の数字が1~8の場合
        else:
            L.append(int(s+str(last-1)))
            L.append(int(s+str(last+1)))
    #出力
    print(L[K-1])

=======
Suggestion 4

def f(n):
    if n == 0:
        return ['0']
    if n == 1:
        return ['1']
    if n == 2:
        return ['2']
    if n == 3:
        return ['3']
    if n == 4:
        return ['4']
    if n == 5:
        return ['5']
    if n == 6:
        return ['6']
    if n == 7:
        return ['7']
    if n == 8:
        return ['8']
    if n == 9:
        return ['9']
    if n == 10:
        return ['10']
    if n == 11:
        return ['11']
    if n == 12:
        return ['12']
    if n == 13:
        return ['13']
    if n == 14:
        return ['14']
    if n == 15:
        return ['15']
    if n == 16:
        return ['16']
    if n == 17:
        return ['17']
    if n == 18:
        return ['18']
    if n == 19:
        return ['19']
    if n == 20:
        return ['20']
    if n == 21:
        return ['21']
    if n == 22:
        return ['22']
    if n == 23:
        return ['23']
    if n == 24:
        return ['24']
    if n == 25:
        return ['25']
    if n == 26:
        return ['26']
    if n == 27:
        return ['27']
    if n == 28:
        return ['28']
    if n == 29:
        return ['29']
    if n == 30:
        return ['30']
    if n == 31:
        return ['31']
    if n == 32:
        return ['32']
    if n == 33:
        return ['33']
    if n == 34:
        return ['34']
    if n == 35:
        return ['35']
    if n == 36:
        return ['36']
    if n == 37:
        return ['37']
    if n == 38:
        return ['38']
    if n == 39:
        return ['39']
    if n == 40:
        return ['40']
    if n ==

=======
Suggestion 5

def runrun(n):
    if n > 10**9:
        return
    yield n
    a = n % 10
    for b in [a-1, a, a+1]:
        if 0 <= b <= 9:
            yield from runrun(10*n+b)

K = int(input())
print(sorted(runrun(n)) [K-1])

=======
Suggestion 6

def main():
    K = int(input())
    ans = 0
    ans_list = []
    for i in range(1, 10):
        ans_list.append(i)
    while len(ans_list) < K:
        ans = ans_list.pop(0)
        for i in range(-1, 2):
            if 0 <= ans % 10 + i <= 9:
                ans_list.append(ans * 10 + ans % 10 + i)
    print(ans_list[K - 1])

=======
Suggestion 7

def main():
    K = int(input())
    #ルンルン数を格納するリスト
    runrun_list = []
    #ルンルン数の個数
    runrun_num = 0
    #ルンルン数を探索するためのリスト
    search_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #ルンルン数の個数が K に達するまでルンルン数を探索する
    while runrun_num < K:
        #探索リストの先頭の数字を取り出し
        num = search_list.pop(0)
        #ルンルン数の個数を 1 増やす
        runrun_num += 1
        #ルンルン数の個数が K に達したらルンルン数を出力してプログラムを終了する
        if runrun_num == K:
            print(num)
            return
        #ルンルン数をリストに追加する
        runrun_list.append(num)
        #ルンルン数の末尾の数字を取り出す
        num_tail = num % 10
        #ルンルン数の末尾の数字が 0 でないとき
        if num_tail != 0:
            #ルンルン数に 1 を足した数を探索リストに追加する
            search_list.append(num * 10 + num_tail - 1)
        #ルンルン数の末尾の数字が 9 でないとき
        if num_tail != 9:
            #ルンルン数に 1 を足した数を探索リストに追加する
            search_list.append(num * 10 + num_tail + 1)

=======
Suggestion 8

def main():
    K = int(input())
    #ルンルン数のリスト
    runrun_list = []
    #ルンルン数のリストの長さ
    runrun_len = 0
    #ルンルン数のリストの長さがKを超えるまでループ
    while runrun_len < K:
        #ルンルン数のリストの長さが0の時
        if runrun_len == 0:
            #ルンルン数のリストに0を追加
            runrun_list.append(0)
            #ルンルン数のリストの長さに1を加算
            runrun_len += 1
        #ルンルン数のリストの長さが0ではない時
        else:
            #ルンルン数のリストの末尾の値を取得
            num = runrun_list[-1]
            #ルンルン数のリストの末尾の値が9の時
            if num % 10 == 9:
                #ルンルン数のリストに末尾の値に10を加算した値を追加
                runrun_list.append(num + 10)
                #ルンルン数のリストの長さに1を加算
                runrun_len += 1
            #ルンルン数のリストの末尾の値が9ではない時
            else:
                #ルンルン数のリストに末尾の値に1を加算した値を追加
                runrun_list.append(num + 1)
                #ルンルン数のリストの長さに1を加算
                runrun_len += 1
                #ルンルン数のリストの末尾の値が0の時
                if num % 10 == 0:
                    #ルンルン数のリストに末尾の値に10を加算した値を追加
                    runrun_list.append(num + 10)
                    #ルンルン数のリ

=======
Suggestion 9

def main():
    K = int(input())
    #ルンルン数を格納するリスト
    runrun_list = []
    #ルンルン数の数
    runrun_count = 0
    #ルンルン数を探す
    for i in range(1, 10):
        #ルンルン数を格納するスタック
        stack = [i]
        while len(stack) > 0:
            #スタックから取り出す
            num = stack.pop()
            #ルンルン数をリストに追加
            runrun_list.append(num)
            runrun_count += 1
            #ルンルン数の数がKを超えたらルンルン数の探索を終了
            if runrun_count > K:
                break
            #ルンルン数のリストの最後の数字の1の位を取得
            last_num = num % 10
            #ルンルン数のリストの最後の数字の1の位が0の場合、1を足した数をスタックに追加
            if last_num == 0:
                stack.append(num * 10 + last_num + 1)
            #ルンルン数のリストの最後の数字の1の位が9の場合、1を引いた数をスタックに追加
            elif last_num == 9:
                stack.append(num * 10 + last_num - 1)
            #ルンルン数のリストの最後の数字の1の位が0でも9でもない場合、1を足した数と1を引いた数をスタックに追加
            else:
                stack.append(num * 10 + last_num + 1)
                stack.append(num * 10 + last_num - 1)
    #ルンルン数のリストのK番目の数字を出力
    print(runrun_list[K - 1])

=======
Suggestion 10

def main():
    K = int(input())
    #K = 100000
    #K = 1
    #K = 13
    #K = 15

    #ルンルン数を格納するリスト
    runrun_list = []
    #ルンルン数を格納するリストの要素数
    runrun_list_length = 0
    #ルンルン数を格納するリストの最後の要素
    runrun_list_last = 0
    #ルンルン数を格納するリストの最後の要素の桁数
    runrun_list_last_digit = 0
    #ルンルン数を格納するリストの最後の要素の最後の桁
    runrun_list_last_digit_last = 0

    #ルンルン数を格納するリストに1を追加
    runrun_list.append(1)
    runrun_list_length += 1
    runrun_list_last = 1
    runrun_list_last_digit = 1
    runrun_list_last_digit_last = 1

    #ルンルン数を格納するリストに2を追加
    runrun_list.append(2)
    runrun_list_length += 1
    runrun_list_last = 2
    runrun_list_last_digit = 1
    runrun_list_last_digit_last = 2

    #ルンルン数を格納するリストに3を追加
    runrun_list.append(3)
    runrun_list_length += 1
    runrun_list_last = 3
    runrun_list_last_digit = 1
    runrun_list_last_digit_last = 3

    #ルンルン数を格納するリストに4を追加
    runrun_list.append(4)
    runrun_list_length += 1
    runrun_list_last = 4
    runrun_list_last_digit = 1
    runrun_list_last_digit_last = 4

    #ルンルン数を格納するリストに5を追加
    runrun_list.append(5)
    runrun_list_length += 1
