Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(n,k,ab):
    ab.sort(key=lambda x:x[0])
    sum = k
    for i in range(n):
        if sum >= ab[i][0]:
            sum += ab[i][1]
        else:
            return sum
    return sum

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    d = {}
    for i in range(N):
        A, B = map(int, input().split())
        if A not in d:
            d[A] = B
        else:
            d[A] += B
    d = sorted(d.items(), key=lambda x:x[0])
    for i in range(len(d)):
        if d[i][0] > K:
            break
        else:
            K += d[i][1]
    print(K)

=======
Suggestion 3

def main():
    N,K = map(int,input().split())
    AB = []
    for i in range(N):
        A,B = map(int,input().split())
        AB.append([A,B])
    AB.sort()
    money = K
    for i in range(N):
        if money >= AB[i][0]:
            money += AB[i][1]
        else:
            print(money)
            break
    else:
        print(money)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    friends = []
    for i in range(N):
        A, B = map(int, input().split())
        friends.append((A, B))
    friends.sort()
    money = K
    for i in range(N):
        if money >= friends[i][0]:
            money += friends[i][1]
    print(money)

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(n)]
    ab.sort()
    ans = 0
    for a,b in ab:
        if a > k:
            break
        k -= b
        ans = a
    print(ans+k)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort()
    for i in range(n):
        if k >= ab[i][0]:
            k += ab[i][1]
    print(k)

=======
Suggestion 7

def main():
    n,k = map(int, input().split())
    friends = []
    for i in range(n):
        friends.append(list(map(int, input().split())))
    friends.sort(key=lambda x: x[0])
    money = k
    current = 0
    for i in range(n):
        if money >= friends[i][0] - current:
            money += friends[i][1]
        else:
            print(current + money)
            return
        current = friends[i][0]
    print(current + money)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A_B = [list(map(int, input().split())) for _ in range(N)]
    A_B.sort()
    now = 0
    for i in range(N):
        if A_B[i][0] - now <= K:
            K -= A_B[i][0] - now
            K += A_B[i][1]
            now = A_B[i][0]
        else:
            now += K
            break
    print(now + K)
main()

=======
Suggestion 9

def main():
    N,K=map(int,input().split())
    A=[]
    B=[]
    for i in range(N):
        a,b=map(int,input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #print(N)
    #print(K)
    #print(len(A))
    #print(len(B))
    #print(max(A))
    #print(min(A))
    #print(max(B))
    #print(min(B))
    #print(A.index(max(A)))
    #print(A.index(min(A)))
    #print(B.index(max(B)))
    #print(B.index(min(B)))
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
    #print

=======
Suggestion 10

def main():
    #输入
    N,K = map(int,input().split())
    AB = [list(map(int,input().split())) for i in range(N)]
    #AB = [[2,1],[5,10]]
    #N,K = 2,3
    #AB = [[5,5],[2,1],[2,2]]
    #AB = [[1,1000000000],[2,1000000000],[3,1000000000],[4,1000000000],[5,1000000000]]
    #N,K = 5,1000000000

    #AB = [[1,1],[2,1],[3,1],[4,1],[5,1]]
    #N,K = 5,3

    #AB = [[1,1],[2,1],[3,1],[4,1],[5,1]]
    #N,K = 5,6

    #AB = [[1,1],[2,1],[3,1],[4,1],[5,1]]
    #N,K = 5,5

    #AB = [[1,1],[2,1],[3,1],[4,1],[5,1]]
    #N,K = 5,4

    #AB = [[1,1],[2,1],[3,1],[4,1],[5,1]]
    #N,K = 5,3

    #AB = [[1,1],[2,1],[3,1],[4,1],[5,1]]
    #N,K = 5,2

    #AB = [[1,1],[2,1],[3,1],[4,1],[5,1]]
    #N,K = 5,1

    #AB = [[1,1],[2,1],[3,1],[4,1],[5,1]]
    #N,K = 5,0

    #AB = [[1,1],[2,1],[3,1],[4,1],[5,1]]
    #N,K = 5,-1

    #AB = [[1,1],[2,1],[3,1],[4,1],[5,1]]
    #N,K = 5,-2

    #AB = [[1,1],[2,1],[3,1],[4,1],[5,1
