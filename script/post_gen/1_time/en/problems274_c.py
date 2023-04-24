Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * (2 ** (N + 1))
    for i in range(N):
        ans[A[i]] = ans[A[i] // 2] + 1

    for i in range(1, 2 ** (N + 1)):
        print(ans[i])

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    dist = [0] * (2 ** (N + 1))
    for i in range(N):
        dist[A[i]] = 1
    for i in range(1, 2 ** (N + 1)):
        if dist[i] == 0:
            dist[i] = dist[i // 2] + 1
    print('

'.join(map(str, dist[1:])))

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = [0] * (2**N+1)
    for i in range(N):
        ans[A[i]] += 1
        ans[A[i]*2] += ans[A[i]]
        ans[A[i]*2+1] += ans[A[i]]
        ans[A[i]] = 0
    for i in range(1, 2**N+1):
        print(ans[i])

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    dist = [0] * (2 * N + 1)
    for i in range(N):
        dist[A[i]] = 0
        dist[2 * A[i]] = dist[A[i]] + 1
        dist[2 * A[i] + 1] = dist[A[i]] + 1
    print(*dist[1:], sep='

')

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a-1 for a in A]
    A = [0] + A
    ans = [0] * (2**N)
    for i in range(1, 2**N):
        ans[i] = ans[A[i]] + 1
    for a in ans:
        print(a)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # A = [1, 3, 5, 2]
    # N = 4
    # print(A)
    # print(N)
    # 1 3 5 2
    # 1 2 4 8 16 32
    # 2 4 8 16 32
    # 4 8 16 32
    # 8 16 32
    # 16 32
    # 32
    # print(2 ** 0)
    # print(2 ** 1)
    # print(2 ** 2)
    # print(2 ** 3)
    # print(2 ** 4)
    # print(2 ** 5)
    # print(2 ** 6)
    # print(2 ** 7)
    # print(2 ** 8)
    # print(2 ** 9)
    # print(2 ** 10)
    # print(2 ** 11)
    # print(2 ** 12)
    # print(2 ** 13)
    # print(2 ** 14)
    # print(2 ** 15)
    # print(2 ** 16)
    # print(2 ** 17)
    # print(2 ** 18)
    # print(2 ** 19)
    # print(2 ** 20)
    # print(2 ** 21)
    # print(2 ** 22)
    # print(2 ** 23)
    # print(2 ** 24)
    # print(2 ** 25)
    # print(2 ** 26)
    # print(2 ** 27)
    # print(2 ** 28)
    # print(2 ** 29)
    # print(2 ** 30)
    # print(2 ** 31)
    # print(2 ** 32)
    # print(2 ** 33)
    # print(2 ** 34)
    # print(2 ** 35)
    # print(2 ** 36)
    # print(2 ** 37)
    # print(2 ** 38)
    # print(2 ** 39)
    # print(2 ** 40)
    # print(2 ** 41

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int,input().split()))
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
    #print(A[64])
    #print(A[65])
    #print(A

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 深さを保持するリスト
    depth = [0] * (2**N+1)

    # 深さを求める
    for i in range(N):
        depth[A[i]] = 1

    for i in range(2, 2**N+1):
        depth[i] = depth[i//2] + 1

    for i in range(1, 2**N+1):
        print(depth[i])

=======
Suggestion 9

def main():
    N = int(input())
    #print(N)
    A = list(map(int, input().split()))
    #print(A)
    #print(len(A))
    #print(A[0])
    #print(A[1])
    
    #print(A)
    #print(len(A))
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    
    #print(A[0])
    #

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 1から出発するとすると、
    # 2^0, 2^1, 2^2, ... 2^N-1, 2^N, 2^N+1
    # つまり、N+2個の要素を持つリストを作る
    # 0, 1, 2, ... N-1, N, N+1

    # 2^0, 2^1, 2^2, ... 2^N-1, 2^N, 2^N+1
    # と、
    # 1, 2, 3, ... N, N+1, N+2
    # は、
    # 1, 2, 4, ... 2^N, 2^N+1, 2^N+2
    # と、
    # 1, 2, 3, ... N, N+1, N+2
    # が等しいことに注意
    # つまり、
    # 1, 2, 4, ... 2^N, 2^N+1, 2^N+2
    # と、
    # 1, 2, 3, ... N, N+1, N+2
    # から、
    # 1, 2, 4, ... 2^N, 2^N+1, 2^N+2
    # と、
    # 0, 1, 2, ... N-1, N, N+1
    # が等しいことになる

    # つまり、
    # 1, 2, 3, ... N, N+1, N+2
    # と、
    # 0, 1, 2, ... N-1, N, N+1
    # の差分が、
    # 1, 2, 4, ... 2^N, 2^N+1, 2^N+2
