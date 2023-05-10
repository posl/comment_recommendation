Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if p[i] != i + 1:
            count += 1
    if count <= 2:
        print('YES')
    else:
        print('NO')

=======
Suggestion 2

def main():
    N = int(input())
    p = list(map(int, input().split()))
    sorted_p = sorted(p)
    count = 0
    for i in range(N):
        if p[i] != sorted_p[i]:
            count += 1
    if count <= 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 3

def main():
    N = int(input())
    p = list(map(int, input().split()))
    p_sorted = sorted(p)
    count = 0
    for i in range(N):
        if p[i] != p_sorted[i]:
            count += 1
    if count == 2 or count == 0:
        print('YES')
    else:
        print('NO')

=======
Suggestion 4

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if p[i] != i+1:
            count += 1
    if count <= 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 5

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = [i for i in range(1, n+1)]
    if p == q:
        print('YES')
    else:
        print('NO')

=======
Suggestion 6

def main():
    N = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if p[i] != i+1:
            cnt += 1
    if cnt <= 2:
        print('YES')
    else:
        print('NO')

=======
Suggestion 7

def main():
    N = int(input())
    p = list(map(int, input().split()))
    #print(N)
    #print(p)
    #print(p[0])
    #print(p[1])
    #print(p[2])
    #print(p[3])
    #print(p[4])
    #print(p[5])
    #print(p[6])
    #print(p[7])
    #print(p[8])
    #print(p[9])
    #print(p[10])
    #print(p[11])
    #print(p[12])
    #print(p[13])
    #print(p[14])
    #print(p[15])
    #print(p[16])
    #print(p[17])
    #print(p[18])
    #print(p[19])
    #print(p[20])
    #print(p[21])
    #print(p[22])
    #print(p[23])
    #print(p[24])
    #print(p[25])
    #print(p[26])
    #print(p[27])
    #print(p[28])
    #print(p[29])
    #print(p[30])
    #print(p[31])
    #print(p[32])
    #print(p[33])
    #print(p[34])
    #print(p[35])
    #print(p[36])
    #print(p[37])
    #print(p[38])
    #print(p[39])
    #print(p[40])
    #print(p[41])
    #print(p[42])
    #print(p[43])
    #print(p[44])
    #print(p[45])
    #print(p[46])
    #print(p[47])
    #print(p[48])
    #print(p[49])
    #print(p[50])
    #print(p[51])
    #print(p[52])
    #print(p[53])
    #print(p[54])
    #print(p[55])
    #print(p[56])
    #print(p[57])
    #print(p[58])
    #print(p[59])
    #print(p[60])
    #print(p[61])
    #print(p[62])
    #print(p[63])
    #print(p[64])
    #print(p[65])
    #print(p[66])
    #

=======
Suggestion 8

def main():
    n = int(input())
    p_list = list(map(int, input().split()))
    p_list_sorted = sorted(p_list)
    count = 0
    for i in range(n):
        if p_list[i] != p_list_sorted[i]:
            count += 1
    if count == 2 or count == 0:
        print('YES')
    else:
        print('NO')

=======
Suggestion 9

def main():
    n = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    for i in range(n-1):
        if p[i] != i+1:
            cnt += 1
    if cnt > 2:
        print('NO')
    else:
        print('YES')
