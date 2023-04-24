Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    L = int(input())
    if L == 2:
        print(4, 4)
        print(1, 2, 0)
        print(1, 3, 1)
        print(2, 4, 0)
        print(3, 4, 0)
    elif L == 3:
        print(4, 5)
        print(1, 2, 0)
        print(2, 3, 0)
        print(3, 4, 0)
        print(1, 3, 1)
        print(3, 4, 1)
    elif L == 4:
        print(8, 10)
        print(1, 2, 0)
        print(2, 3, 0)
        print(3, 4, 0)
        print(1, 5, 0)
        print(2, 6, 0)
        print(3, 7, 0)
        print(4, 8, 0)
        print(5, 6, 1)
        print(6, 7, 1)
        print(7, 8, 1)
    else:
        print(3 * L - 2, 3 * L - 3)
        for i in range(L - 1):
            print(i + 1, i + 2, 0)
        for i in range(L - 2):
            print(i + 1, i + 3, 1)
        print(1, 2 * L - 2, L - 1)
        print(2 * L - 3, 3 * L - 3, L - 1)

=======
Suggestion 2

def main():
    L = int(input())
    ans = []
    ans.append([1,2,0])
    ans.append([2,3,0])
    ans.append([3,4,0])
    ans.append([1,5,0])
    ans.append([2,6,0])
    ans.append([3,7,0])
    ans.append([4,8,0])
    ans.append([5,6,1])
    ans.append([6,7,1])
    ans.append([7,8,1])
    for i in range(2,L):
        ans.append([i,i+3,i-1])
        ans.append([i+3,i+4,0])
    print(len(ans),len(ans))
    for a in ans:
        print(*a)

=======
Suggestion 3

def main():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    print(1, 2, 0)
    print(2, 3, 0)
    print(3, 4, 0)
    print(1, 5, 0)
    print(2, 6, 0)
    print(3, 7, 0)
    print(4, 8, 0)
    print(5, 6, 1)
    print(6, 7, 1)
    print(7, 8, 1)
    for i in range(3, N):
        print(i, i+1, 0)
    for i in range(N, N+L-1):
        print(i, i+1, 1)

=======
Suggestion 4

def main():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(1, N):
        print(i, i + 1, 0)
    for i in range(1, N):
        print(i, i + 1, 10 ** 6)
    for i in range(N - 1, 0, -1):
        if L <= 10 ** 6:
            print(i, N, L)
            L = 0
        else:
            print(i, N, 10 ** 6)
            L -= 10 ** 6

=======
Suggestion 5

def main():
    L = int(input())
    print(2 * L + 2, 2 * L + 1)
    for i in range(L + 1):
        print(i + 1, i + 2, 0)
    for i in range(L):
        print(i + 1, i + 2, 1)
    print(L + 1, L + 2, 0)

=======
Suggestion 6

def main():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(N):
        print(i+1, i+2, 0)
    for i in range(N-1):
        print(i+1, i+3, 0)
    for i in range(N-2):
        print(i+1, i+4, 0)
    for i in range(N-3):
        print(i+1, i+5, 0)
    for i in range(N-4):
        print(i+1, i+6, 0)
    for i in range(N-5):
        print(i+1, i+7, 0)
    for i in range(N-6):
        print(i+1, i+8, 0)
    for i in range(N-7):
        print(i+1, i+9, 0)
    for i in range(N-8):
        print(i+1, i+10, 0)
    for i in range(N-9):
        print(i+1, i+11, 0)
    for i in range(N-10):
        print(i+1, i+12, 0)
    for i in range(N-11):
        print(i+1, i+13, 0)
    for i in range(N-12):
        print(i+1, i+14, 0)
    for i in range(N-13):
        print(i+1, i+15, 0)
    for i in range(N-14):
        print(i+1, i+16, 0)
    for i in range(N-15):
        print(i+1, i+17, 0)
    for i in range(N-16):
        print(i+1, i+18, 0)
    for i in range(N-17):
        print(i+1, i+19, 0)
    for i in range(N-18):
        print(i+1, i+20, 0)
    for i in range(L-1):
        print(i+1, i+2, i+1)

=======
Suggestion 7

def main():
    L = int(input())
    if L % 2 == 0:
        print(L//2+1)
        for i in range(L//2):
            print(i+1,i+2)
        print(L//2+1,L)
    else:
        print((L+1)//2)
        for i in range((L+1)//2-1):
            print(i+1,i+2)
        print((L+1)//2,L)

=======
Suggestion 8

def main():
    L = int(input())

    if L % 2 == 0:
        N = 2 * L
        M = 3 * L
        print(N, M)
        for i in range(1, L + 1):
            print(i, i + L, 0)
            print(i, i + L, 1)
            print(i, i + L, 2)
    else:
        N = 2 * L + 1
        M = 3 * L + 1
        print(N, M)
        for i in range(1, L + 1):
            print(i, i + L, 0)
            print(i, i + L, 1)
            print(i, i + L, 2)
        print(1, N, 0)

=======
Suggestion 9

def main():
    L = int(input())
    N = 2*L
    M = 2*L-1
    print(N,M)
    for i in range(1,N):
        print(i,i+1,0)
    for i in range(1,L+1):
        print(i,N-i+1,i)

=======
Suggestion 10

def main():
    L = int(input())
    # 1 から L+1 までの頂点を用意
    # 1 から頂点 i までのパスの長さは i-1
    # 1 から頂点 i までのパスの数は L-i+1
    # 1 から頂点 i までのパスの数が 1 以上の場合、1 から頂点 i までのパスの長さは i-1 以上 L-1 以下
    # 1 から頂点 i までのパスの数が 2 以上の場合、1 から頂点 i までのパスの長さは i-1 以上 L-2 以下
    # 1 から頂点 i までのパスの数が 3 以上の場合、1 から頂点 i までのパスの長さは i-1 以上 L-3 以下
    # ...
    # 1 から頂点 i までのパスの数が L-i+1 以上の場合、1 から頂点 i までのパスの長さは i-1 以上 L-(L-i+1) 以下
    # 1 から頂点 i までのパスの数が L-i+1 未満の場合、1 から頂点 i までのパスの長さは i-1 以上 L-(L-i+1)-1 以下
    # 1 から頂点 i までのパスの数が 0 の場合、1 から頂点 i までのパスの長さは i-1 以上 L-(L-i+1)-1 以下
    # 1 から頂点 i までのパスの数が 1 の場合、1 から頂点 i までのパスの長さは i-1 以上 L-(L-i+1)-1-1 以下
    # 1
