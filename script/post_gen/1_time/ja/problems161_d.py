Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    if N == 1:
        print(1)
        return
    if N == 2:
        print(2)
        return
    if N == 3:
        print(3)
        return
    N -= 3
    for i in range(1, 10):
        for j in range(10):
            for k in range(10):
                if abs(j - k) <= 1:
                    N -= 1
                    if N == 0:
                        print(str(i) + str(j) + str(k))
                        return

=======
Suggestion 2

def main():
    K = int(input())
    count = 0
    for i in range(1, 10):
        count += 1
        if count == K:
            print(i)
            return
        for j in range(0, 10):
            count += 1
            if count == K:
                print(int(str(i)+str(j)))
                return
            for k in range(0, 10):
                count += 1
                if count == K:
                    print(int(str(i)+str(j)+str(k)))
                    return
                for l in range(0, 10):
                    count += 1
                    if count == K:
                        print(int(str(i)+str(j)+str(k)+str(l)))
                        return
                    for m in range(0, 10):
                        count += 1
                        if count == K:
                            print(int(str(i)+str(j)+str(k)+str(l)+str(m)))
                            return
                        for n in range(0, 10):
                            count += 1
                            if count == K:
                                print(int(str(i)+str(j)+str(k)+str(l)+str(m)+str(n)))
                                return
                            for o in range(0, 10):
                                count += 1
                                if count == K:
                                    print(int(str(i)+str(j)+str(k)+str(l)+str(m)+str(n)+str(o)))
                                    return
                                for p in range(0, 10):
                                    count += 1
                                    if count == K:
                                        print(int(str(i)+str(j)+str(k)+str(l)+str(m)+str(n)+str(o)+str(p)))
                                        return
                                    for q in range(0, 10):
                                        count += 1
                                        if count == K:
                                            print(int(str(i)+str(j)+str(k)+str(l)+str(m)+str(n)+str(o)+str(p)+str(q)))
                                            return
                                        for r in range(0, 10):
                                            count += 1
                                            if count == K:
                                                print(int(str(i)+str(j)+str(k)+str(l)+str(m)+str(n)+str(o)+str(p)+str(q)+str(r)))
                                                return
                                            for s in range(0, 10):
                                                count += 1
                                                if count == K:
                                                    print(int(str(i)+str(j)+str

=======
Suggestion 3

def runrun(n):
    if n > 10**9:
        return
    if n > 0:
        runrun_list.append(n)
    runrun(n*10 + n%10 - 1)
    runrun(n*10 + n%10)
    runrun(n*10 + n%10 + 1)

runrun_list = []
runrun(0)

K = int(input())
print(sorted(runrun_list)[K-1])

=======
Suggestion 4

def main():
    K = int(input())
    ans = ""
    ans = ans + str(1)
    ans = ans + str(2)
    ans = ans + str(3)
    ans = ans + str(4)
    ans = ans + str(5)
    ans = ans + str(6)
    ans = ans + str(7)
    ans = ans + str(8)
    ans = ans + str(9)
    ans = ans + str(10)
    ans = ans + str(11)
    ans = ans + str(12)
    ans = ans + str(21)
    ans = ans + str(22)
    ans = ans + str(23)
    print(ans)
    ans = ans + str(32)
    ans = ans + str(33)
    ans = ans + str(34)
    ans = ans + str(35)
    ans = ans + str(36)
    ans = ans + str(37)
    ans = ans + str(38)
    ans = ans + str(39)
    ans = ans + str(40)
    ans = ans + str(41)
    ans = ans + str(42)
    ans = ans + str(51)
    ans = ans + str(52)
    ans = ans + str(53)
    ans = ans + str(54)
    ans = ans + str(55)
    ans = ans + str(56)
    ans = ans + str(57)
    ans = ans + str(58)
    ans = ans + str(59)
    ans = ans + str(60)
    ans = ans + str(61)
    ans = ans + str(62)
    ans = ans + str(71)
    ans = ans + str(72)
    ans = ans + str(73)
    ans = ans + str(74)
    ans = ans + str(75)
    ans = ans + str(76)
    ans = ans + str(77)
    ans = ans + str(78)
    ans = ans + str(79)
    ans = ans + str(80)
    ans = ans + str(81)
    ans = ans + str(82)
    ans = ans + str(91)
    ans = ans + str(92)
    ans = ans + str(93)
    ans = ans + str(

=======
Suggestion 5

def main():
    #Kを取得
    K = int(input())
    #ルンルン数を格納するリストを作成
    runrun_list = []
    #ルンルン数を格納するリストの長さがKになるまでループ
    while len(runrun_list) < K:
        #ルンルン数を格納するリストの長さが0の場合
        if len(runrun_list) == 0:
            #0~9をルンルン数を格納するリストに格納
            for i in range(10):
                runrun_list.append(i)
        #ルンルン数を格納するリストの長さが0以外の場合
        else:
            #ルンルン数を格納するリストの長さを取得
            runrun_list_len = len(runrun_list)
            #ルンルン数を格納するリストの長さ分ループ
            for i in range(runrun_list_len):
                #ルンルン数を格納するリストの最後の要素を取得
                last_num = runrun_list[-1]
                #ルンルン数を格納するリストの最後の要素の最後の桁を取得
                last_num_last_digit = last_num % 10
                #ルンルン数を格納するリストの最後の要素の最後の桁が0の場合
                if last_num_last_digit == 0:
                    #ルンルン数を格納するリストに最後の要素に10を足した値を追加
                    runrun_list.append(last_num + 10)
                #ルンルン数を格納するリストの最後の要素の最後の桁が9の場合
                elif last_num_last_digit == 9:
                    #ルンルン数を格納するリストに最後の要素に10を引いた値を追加
                    runrun_list.append(last_num - 10)
                #ルンルン

=======
Suggestion 6

def main():
    K = int(input())
    
    def runrun(n):
        if n < 10:
            return True
        else:
            return (abs(int(str(n)[-1]) - int(str(n)[-2])) <= 1) and runrun(n // 10)
    
    def runrun_list(n):
        if n < 10:
            return [n]
        else:
            return [i for i in runrun_list(n // 10) if abs(int(str(n)[-1]) - int(str(i)[-1])) <= 1]
    
    def runrun_num(n):
        if n == 1:
            return 1
        else:
            return runrun_num(n - 1) + len(runrun_list(10 ** (n - 1)))
    
    def runrun_ans(n):
        if n < 10:
            return n
        else:
            return runrun_ans(n - 1) + len(runrun_list(10 ** (n - 1)))
    
    def runrun_k(k):
        if k <= 0:
            return 0
        elif k <= 9:
            return k
        else:
            for i in range(1, 10):
                if runrun_num(i) >= k:
                    return runrun_ans(i - 1) + runrun_list(10 ** (i - 1))[k - runrun_num(i - 1) - 1]
    
    print(runrun_k(K))

=======
Suggestion 7

def main():
    K = int(input())
    #print(K)

    #ルンルン数を格納するリスト
    runrun = []

    #ルンルン数の探索
    #1桁目は1～9
    for i in range(1, 10):
        #print(i)
        runrun.append(i)
        #print(runrun)
        #2桁目は1～9
        for j in range(1, 10):
            #print(j)
            #print(i, j)
            #print(abs(i - j))
            #差の絶対値が1以下の場合のみルンルン数に追加
            if abs(i - j) <= 1:
                runrun.append(int(str(i) + str(j)))
                #print(runrun)
                #3桁目は1～9
                for k in range(1, 10):
                    #print(k)
                    #print(i, j, k)
                    #print(abs(j - k))
                    #差の絶対値が1以下の場合のみルンルン数に追加
                    if abs(j - k) <= 1:
                        runrun.append(int(str(i) + str(j) + str(k)))
                        #print(runrun)
                        #4桁目は1～9
                        for l in range(1, 10):
                            #print(l)
                            #print(i, j, k, l)
                            #print(abs(k - l))
                            #差の絶対値が1以下の場合のみルンルン数に追加
                            if abs(k - l) <= 1:
                                runrun.append(int(str(i) + str(j) + str(k) + str(l)))
                                #print(runrun)
                                #5桁目は1～9
                                for m in range(1, 10):
                                    #print(m)
                                    #print(i, j, k, l, m)
                                    #print(abs(l - m))
                                    #差の絶対値が1以下の場合のみルンルン数に追加
                                    if abs(l - m) <= 1:
                                        runrun.append(int(str(i) + str

=======
Suggestion 8

def runrun(k):
    #k番目のルンルン数を求める
    #ルンルン数は1桁から始まり、2桁、3桁と増えていく
    #ルンルン数は1桁目は1から始まり、2桁目は0から9までの数字が使える
    #3桁目以降は、前の桁の値-1,0,1のいずれかを使う
    #ルンルン数は大きい方から数える
    #ルンルン数は前のルンルン数の次のルンルン数から始まる
    #ルンルン数は1桁から始まり、2桁、3桁と増えていく

    #ルンルン数は前のルンルン数の次のルンルン数から始まる
    #ルンルン数は1桁から始まり、2桁、3桁と増えていく
    #ルンルン数は1桁目は1から始まり、2桁目は0から9までの数字が使える
    #3桁目以降は、前の桁の値-1,0,1のいずれかを使う
    #ルンルン数は大きい方から数える
    #ルンルン数は前のルンルン数の次のルンルン数から始まる

    #ルンルン数は前のルンルン数の次のルンルン数から始まる
    #ルンルン数は1桁から始まり、2桁、3桁と増えていく
    #ルンルン数は1桁目は1から始まり、2桁目は0から9までの数字が使える
    #3桁目以降は、前の桁の値-1,0,1のいずれかを使う

=======
Suggestion 9

def main():
    K = int(input())
    print(solve(K))
