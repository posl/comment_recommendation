Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    #print(a)
    m = a[0] - 1
    #print(m)
    cnt = 0
    while True:
        #print(m)
        for i in range(n):
            cnt += m % a[i]
        if cnt > m:
            break
        else:
            cnt = 0
            m += 1
    print(m)

=======
Suggestion 2

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    #print(a)
    f = 0
    for i in range(n):
        f += a[i] * (n - i - 1)
        #print(f)
    print(f)
main()

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    #a.sort()
    #a.reverse()
    #print(a)
    #print(a[0])
    #print(a[1])
    #print(a[2])
    #print(a[3])
    #print(a[4])
    #print(a[5])
    #print(a[6])
    #print(a[7])
    #print(a[8])
    #print(a[9])
    #print(a[10])
    #print(a[11])
    #print(a[12])
    #print(a[13])
    #print(a[14])
    #print(a[15])
    #print(a[16])
    #print(a[17])
    #print(a[18])
    #print(a[19])
    #print(a[20])
    #print(a[21])
    #print(a[22])
    #print(a[23])
    #print(a[24])
    #print(a[25])
    #print(a[26])
    #print(a[27])
    #print(a[28])
    #print(a[29])
    #print(a[30])
    #print(a[31])
    #print(a[32])
    #print(a[33])
    #print(a[34])
    #print(a[35])
    #print(a[36])
    #print(a[37])
    #print(a[38])
    #print(a[39])
    #print(a[40])
    #print(a[41])
    #print(a[42])
    #print(a[43])
    #print(a[44])
    #print(a[45])
    #print(a[46])
    #print(a[47])
    #print(a[48])
    #print(a[49])
    #print(a[50])
    #print(a[51])
    #print(a[52])
    #print(a[53])
    #print(a[54])
    #print(a[55])
    #print(a[56])
    #print(a[57])
    #print(a[58])
    #print(a[59])
    #print(a[60])
    #print(a[61])
    #print(a[62])
    #print(a[63])
    #print(a[64])
    #print(a[65])
    #print(a

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    ans = 0
    for i in range(a[0]):
        tmp = 0
        for j in range(n):
            tmp += i % a[j]
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += a[i] - 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int,input().split()))
    print(sum([A[i]-1 for i in range(N)]))

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))

    max_val = 0
    for m in range(1, max(A)+1):
        val = 0
        for a in A:
            val += m % a
        if val > max_val:
            max_val = val
    print(max_val)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += a[i]-1
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    #print(N, A)
    
    # 2 <= N <= 3000
    # 2 <= a_i <= 10^5
    # 10^5 * 3000 = 3 * 10^8 < 2^28
    # 2^28 なので、2^29 以上の数であれば、どんな数でも割り切れる
    # 2^29 以下の数であれば、2^28 以上の数であれば、どんな数でも割り切れる
    # 2^28 以下の数であれば、2^27 以上の数であれば、どんな数でも割り切れる
    # 2^27 以下の数であれば、2^26 以上の数であれば、どんな数でも割り切れる
    # ...
    # 2^0 以下の数であれば、2^0 以上の数であれば、どんな数でも割り切れる
    # ということは、2^28 から 2^29 以下の数であれば、どんな数でも割り切れる
    # ということは、2^28 以下の数であれば、どんな数でも割り切れる
    # 2^28 以下の数であれば、どんな数でも割り切れる
    # ということは、2^27 以下の数であれば、どんな数でも割り切れる
    # ということは、2^26 以下の数であれば、どんな数でも割り切れる
    # ということは、2^25 以下の数であれば、どんな数でも割り切れる
    # ということは、2^24 以下の数
