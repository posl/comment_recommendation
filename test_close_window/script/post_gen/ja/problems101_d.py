Synthesizing 10/10 solutions

=======

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

=======

def get_sum_of_digit(n):
    sum_of_digit = 0
    while n > 0:
        sum_of_digit += n % 10
        n //= 10
    return sum_of_digit

=======

def main():
    k = int(input())
    l = []
    for i in range(1, 10):
        l.append(i)
    for i in range(1, 10):
        for j in range(10):
            l.append(int(str(i) + str(j)))
    for i in range(1, 10):
        for j in range(10):
            for k in range(10):
                l.append(int(str(i) + str(j) + str(k)))
    for i in range(1, 10):
        for j in range(10):
            for k in range(10):
                for m in range(10):
                    l.append(int(str(i) + str(j) + str(k) + str(m)))
    l.sort()
    for i in range(k):
        print(l[i])

=======

def main():
    K = int(input())
    ans = []
    for i in range(1, 100000):
        s = sum([int(x) for x in str(i)])
        if i % s == 0:
            ans.append(i)
    for i in range(K):
        print(ans[i])

=======

def main():
    K = int(input())
    #1桁の自然数はすぬけ数
    #2桁の自然数はすぬけ数
    #3桁の自然数はすぬけ数
    #4桁の自然数はすぬけ数
    #5桁の自然数はすぬけ数
    #6桁の自然数はすぬけ数
    #7桁の自然数はすぬけ数
    #8桁の自然数はすぬけ数
    #9桁の自然数はすぬけ数
    #10桁の自然数はすぬけ数
    #11桁の自然数はすぬけ数
    #12桁の自然数はすぬけ数
    #13桁の自然数はすぬけ数
    #14桁の自然数はすぬけ数
    #15桁の自然数はすぬけ数
    #16桁の自然数はすぬけ数
    #17桁の自然数はすぬけ数
    #18桁の自然数はすぬけ数
    #19桁の自然数はすぬけ数
    #20桁の自然数はすぬけ数
    #21桁の自然数はすぬけ数
    #22桁の自然数はすぬけ数
    #23桁の自然数はすぬけ数
    #24桁の自然数はすぬけ数
    #25桁の自然数はすぬけ数
    #26桁の自然数はすぬけ数
    #27桁の自然数はすぬけ数
    #28桁の自然数はすぬけ数
    #29桁の自然数はすぬけ数
    #30桁の自然数はすぬけ数
    #31桁の自然数はす

=======

def main():
    K = int(input())
    #すぬけ数を格納する配列
    s_num = []
    #10進数での各桁の和を格納する配列
    s = []
    #すぬけ数を格納する配列に1を格納
    s_num.append(1)
    #10進数での各桁の和を格納する配列に1を格納
    s.append(1)
    #すぬけ数を格納する配列に2を格納
    s_num.append(2)
    #10進数での各桁の和を格納する配列に2を格納
    s.append(2)
    #すぬけ数を格納する配列に3を格納
    s_num.append(3)
    #10進数での各桁の和を格納する配列に3を格納
    s.append(3)
    #すぬけ数を格納する配列に4を格納
    s_num.append(4)
    #10進数での各桁の和を格納する配列に4を格納
    s.append(4)
    #すぬけ数を格納する配列に5を格納
    s_num.append(5)
    #10進数での各桁の和を格納する配列に5を格納
    s.append(5)
    #すぬけ数を格納する配列に6を格納
    s_num.append(6)
    #10進数での各桁の和を格納する配列に6を格納
    s.append(6)
    #すぬけ数を格納する配列に7を格納
    s_num.append(7)
    #10進数での各桁の和を格納する配列に7を格納
    s.append(7)
    #すぬけ数を格納する

=======

def main():
    # 入力
    K = int(input())
    # 処理
    ans = []
    for i in range(1,100000):
        if i % 9 == 0:
            ans.append(i)
        else:
            a = i
            while a > 0:
                i += a % 10
                a //= 10
            if i % 9 == 0:
                ans.append(i)
        if len(ans) == K:
            break
    # 出力
    for i in range(K):
        print(ans[i])

=======

def sum_of_digit(n):
    return sum([int(x) for x in str(n)])

=======

def digit_sum(n):
    return sum(map(int, str(n)))

=======

def sum_digit(n):
    return sum(map(int, list(str(n))))
