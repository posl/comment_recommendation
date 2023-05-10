Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    C = []
    for i in range(1,N+1):
        if i % 2 == 0:
            B.append(i)
        else:
            C.append(i)
    print("Yes")
    print(len(B), *B)
    print(len(C), *C)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int,input().split()))
    a = [i%200 for i in a]
    d = dict()
    for i in range(1,1<<n):
        s = 0
        b = []
        for j in range(n):
            if i&(1<<j):
                s += a[j]
                b.append(j+1)
        if s%200 in d:
            print('Yes')
            print(len(d[s%200]),*d[s%200])
            print(len(b),*b)
            return
        else:
            d[s%200] = b
    print('No')

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = [0]*200
    for i in range(n):
        mod[a[i]%200] += 1
    ans = 0
    for i in range(200):
        ans += mod[i]*(mod[i]-1)//2
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int,input().split()))
    if n == 2:
        if a[0] % 200 == a[1] % 200:
            print("Yes")
            print("1 1")
            print("1 2")
            return
        else:
            print("No")
            return
    elif n == 3:
        if a[0] % 200 == a[1] % 200:
            print("Yes")
            print("1 1")
            print("2 2 3")
            return
        elif a[0] % 200 == a[2] % 200:
            print("Yes")
            print("1 1")
            print("2 2 3")
            return
        elif a[1] % 200 == a[2] % 200:
            print("Yes")
            print("1 2")
            print("2 1 3")
            return
        else:
            print("No")
            return
    else:
        for i in range(n):
            for j in range(i+1,n):
                if a[i] % 200 == a[j] % 200:
                    print("Yes")
                    print("1",i+1)
                    print("1",j+1)
                    return
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if a[i] % 200 + a[j] % 200 == a[k] % 200:
                        print("Yes")
                        print("2",i+1,j+1)
                        print("1",k+1)
                        return
        print("No")
        return
main()

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 2:
        if A[0]%200 == A[1]%200:
            print("Yes")
            print(1,1)
            print(1,2)
            exit()
        else:
            print("No")
            exit()
    else:
        dict = {}
        for i in range(2**N):
            s = str(bin(i)[2:])
            s = s.zfill(N)
            #print(s)
            B = []
            C = []
            for j in range(N):
                if s[j] == "0":
                    B.append(j+1)
                else:
                    C.append(j+1)
            #print(B,C)
            sumB = 0
            sumC = 0
            for b in B:
                sumB += A[b-1]
            for c in C:
                sumC += A[c-1]
            #print(sumB, sumC)
            if sumB%200 == sumC%200:
                if sumB%200 in dict:
                    print("Yes")
                    print(len(dict[sumB%200]), *dict[sumB%200])
                    print(len(B), *B)
                    exit()
                else:
                    dict[sumB%200] = B
        print("No")
        exit()

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [i % 200 for i in a]
    b = []
    c = []
    for i in range(1, 2**min(n, 8)):
        sum = 0
        for j in range(min(n, 8)):
            if (i >> j) & 1:
                sum += a[j]
        sum %= 200
        if sum in b:
            c = []
            for j in range(min(n, 8)):
                if (i >> j) & 1:
                    c.append(j + 1)
            break
        else:
            b.append(sum)
    if c == []:
        print('No')
    else:
        print('Yes')
        print(len(b), *b)
        print(len(c), *c)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_mod = [i%200 for i in a]
    #print(a_mod)
    a_mod_count = [0]*200
    for i in a_mod:
        a_mod_count[i] += 1
    #print(a_mod_count)
    ans = "No"
    for i in range(200):
        if a_mod_count[i] > 1:
            ans = "Yes"
            break
    if ans == "No":
        print(ans)
        return
    ans = "Yes"
    for i in range(200):
        if a_mod_count[i] > 1:
            b = a_mod.index(i)+1
            a_mod[a_mod.index(i)] = -1
            c = a_mod.index(i)+1
            print(ans)
            print(1, b)
            print(1, c)
            return
    ans = "Yes"
    for i in range(200):
        if a_mod_count[i] > 1:
            b = a_mod.index(i)+1
            a_mod[a_mod.index(i)] = -1
            c = a_mod.index(i)+1
            print(ans)
            print(1, b)
            print(1, c)
            return
    ans = "Yes"
    for i in range(200):
        if a_mod_count[i] > 1:
            b = a_mod.index(i)+1
            a_mod[a_mod.index(i)] = -1
            c = a_mod.index(i)+1
            print(ans)
            print(1, b)
            print(1, c)
            return
    ans = "Yes"
    for i in range(200):
        if a_mod_count[i] > 1:
            b = a_mod.index(i)+1
            a_mod[a_mod.index(i)] = -1
            c = a_mod.index(i)+1
            print(ans)
            print(1, b)
            print(1, c)
            return
    ans = "Yes"
    for i in range(200):
        if a_mod_count[i] > 1:
            b = a_mod.index(i)+1
            a_mod[a_mod.index(i)] = -1
            c = a_mod.index(i)+1
            print(ans)
            print(1, b)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 1 ≦ B_1 < B_2 < ... < B_{x} ≦ N
    # 1 ≦ C_1 < C_2 < ... < C_{y} ≦ N
    # B と C は、異なる数列である。
    # x ≠ y のとき、または、ある整数 i (1 ≤ i ≤ min(x, y)) が存在して B_i ≠ C_i であるとき、B と C は異なるものとする。
    # A_{B_1} + A_{B_2} + ... + A_{B_x} を 200 で割った余りと A_{C_1} + A_{C_2} + ... + A_{C_y} を 200 で割った余りが等しい。
    # 1 ≦ A_i ≦ 10^9
    # 2 ≦ N ≦ 200

    # 200で割った余りが等しいというのは、200で割った余りが等しいということだから、
    # 200で割った余りを200で割った余りが等しいということになる
    # つまり、200で割った余りを200で割った余りが等しいということは、
    # 200で割った余りを400で割った余りが等しいということになる
    # つまり、200で割った余りを400で割った余りが等しいということは、
    # 200で割った余りを600で割った余りが等しいということになる
    # つまり、200で割った余りを600で割った余りが等しいということは、
    # 200で割った余りを800で

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # dp[i][j] := i番目までの整数の中からいくつか選んで、その総和を200で割った余りがjであるような選び方が存在するかどうか
    dp = [[False] * 200 for _ in range(N+1)]
    dp[0][0] = True

    for i in range(N):
        for j in range(200):
            # i番目の整数を選ぶ場合
            dp[i+1][j] |= dp[i][j]
            # i番目の整数を選ばない場合
            dp[i+1][(j+A[i])%200] |= dp[i][j]

    if dp[N][0] == False:
        print('No')
        return

    print('Yes')
    # dp[N][0] == True となるような選び方を復元する
    ans = []
    i = N
    j = 0
    while i > 0:
        # i番目の整数を選ばなかった場合
        if dp[i-1][j]:
            i -= 1
        # i番目の整数を選んだ場合
        else:
            ans.append(i)
            j = (j - A[i-1]) % 200
            i -= 1

    print(len(ans), *ans)
    i = N
    j = 0
    while i > 0:
        if dp[i-1][j]:
            i -= 1
        else:
            ans.append(i)
            j = (j - A[i-1]) % 200
            i -= 1

    print(len(ans), *ans)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [i%200 for i in A]
    #print(A)
    #print(A.count(0))
    #print(A.count(1))
    #print(A.count(2))
    #print(A.count(3))
    #print(A.count(4))
    #print(A.count(5))
    #print(A.count(6))
    #print(A.count(7))
    #print(A.count(8))
    #print(A.count(9))
    #print(A.count(10))
    #print(A.count(11))
    #print(A.count(12))
    #print(A.count(13))
    #print(A.count(14))
    #print(A.count(15))
    #print(A.count(16))
    #print(A.count(17))
    #print(A.count(18))
    #print(A.count(19))
    #print(A.count(20))
    #print(A.count(21))
    #print(A.count(22))
    #print(A.count(23))
    #print(A.count(24))
    #print(A.count(25))
    #print(A.count(26))
    #print(A.count(27))
    #print(A.count(28))
    #print(A.count(29))
    #print(A.count(30))
    #print(A.count(31))
    #print(A.count(32))
    #print(A.count(33))
    #print(A.count(34))
    #print(A.count(35))
    #print(A.count(36))
    #print(A.count(37))
    #print(A.count(38))
    #print(A.count(39))
    #print(A.count(40))
    #print(A.count(41))
    #print(A.count(42))
    #print(A.count(43))
    #print(A.count(44))
    #print(A.count(45))
    #print(A.count(46))
    #print(A.count(47))
    #print(A.count(48))
    #print(A.count(49))
    #print(A.count(50))
    #print(A.count(51))
    #print(A.count(52))
    #print(A.count(53))
    #print(A.count(54))
    #print(A.count(55))
    #print(A.count(56))
    #print(A.count(57))
