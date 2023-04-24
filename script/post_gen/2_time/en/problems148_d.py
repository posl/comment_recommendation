Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))

    if a[0] != 1:
        print(-1)
        return

    ans = 0
    for i in range(1, n):
        if a[i] == a[i-1]+1:
            continue
        if a[i] > a[i-1]+1:
            print(-1)
            return
        ans += a[i-1]-a[i]+1

    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if A[i] == count + 1:
            count += 1
    if count == 0:
        print(-1)
    else:
        print(N - count)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] == ans + 1:
            ans += 1
    if ans == 0:
        print(-1)
    else:
        print(N - ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] != 1:
        print(-1)
        return
    for i in range(n-1):
        if a[i+1] - a[i] > 1:
            print(-1)
            return
    print(n - a.count(a[0]))

=======
Suggestion 5

def   main (): 
     N   =   int ( input ()) 
     a   =   list ( map ( int ,   input (). split ())) 
     ans   =   0 
     for   i   in   range ( N ): 
         if   a [ i ]   ==   i   +   1 : 
             ans   +=   1 
             a [ i ]   =   0 
     if   ans   ==   N : 
         print ( - 1 ) 
     else : 
         print ( N   -   ans )

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a - 1 for a in A]
    if A[0] != 0:
        print(-1)
        return
    cnt = 0
    for i in range(N - 1):
        if A[i] >= A[i + 1]:
            cnt += A[i] - A[i + 1]
        else:
            if A[i + 1] - A[i] > 1:
                print(-1)
                return
    print(cnt)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a-1 for a in A]
    if A[0] != 0:
        print(-1)
        return
    ans = 0
    for i in range(1, N):
        if A[i] == 0:
            ans += 1
            continue
        if A[i] < A[i-1]:
            print(-1)
            return
        if A[i] == A[i-1]:
            ans += 1
    print(ans)

=======
Suggestion 8

def solve():
    N = int(input())
    A = list(map(int,input().split()))
    if A[0] != 1:
        print(-1)
        return
    else:
        ans = 0
        for i in range(1,N):
            if A[i] == A[i-1]+1:
                continue
            elif A[i] > A[i-1]+1:
                print(-1)
                return
            else:
                ans += 1
        print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
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
    #print(A[63])
    #print(A[64])
    #print(A[65])
    #print(A[66])
    #

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # print(N, A)
    B = []
    for i in range(N):
        B.append((A[i], i))
    B.sort(key=lambda x: x[0])
    # print(B)
    ans = 0
    prev = -1
    for i in range(N):
        if B[i][1] < prev:
            ans += 1
        else:
            prev = B[i][1]
    print(ans)
