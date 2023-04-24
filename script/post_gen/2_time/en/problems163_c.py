Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n - 1):
        b[a[i] - 1] += 1
    print('

'.join(map(str, b)))

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N-1):
        B[A[i]-1] += 1
    for i in range(N):
        print(B[i])

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N-1):
        ans[A[i]-1] += 1
    for i in range(N):
        print(ans[i])

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i]-1] += 1
    for i in range(N):
        print(B[i])

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = [0] * N
    for i in A:
        count[i-1] += 1
    for i in count:
        print(i)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * n
    for i in a:
        cnt[i-1] += 1
    for i in cnt:
        print(i)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sub = [0] * n
    for i in range(n-1):
        sub[a[i]-1] += 1
    for i in range(n):
        print(sub[i])

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)
    B = [0] * N
    for i in range(N-1):
        B[A[i]-1] += 1
    for i in range(N):
        print(B[i])

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int,input().split()))
    if N == 2:
        print(1)
        print(0)
        return
    A.append(0)
    B = [0] * (N+1)
    for i in range(N):
        B[A[i]] += 1
    for i in range(1,N+1):
        print(B[i])

main()

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #A = [int(x) for x in input().split()]
    #print(N)
    #print(A)
    #print(len(A))
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
    #
