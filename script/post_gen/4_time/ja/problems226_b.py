Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split()))[1:])
    a.sort()
    ans = 1
    for i in range(n - 1):
        if a[i] != a[i + 1]:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    L = []
    for i in range(N):
        L.append(list(map(int,input().split())))
    L.sort()
    cnt = 1
    for i in range(N-1):
        if L[i] != L[i+1]:
            cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    # input
    N = int(input())
    LAs = [list(map(int, input().split())) for _ in range(N)]
    # compute
    Ls = [LAs[i][0] for i in range(N)]
    As = [LAs[i][1:] for i in range(N)]
    # output
    print(len(set(tuple(As[i]) for i in range(N))))

=======
Suggestion 4

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split()))[1:])
    a.sort()
    a.append([])
    ans = 0
    for i in range(n):
        if a[i] != a[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    a.sort()
    a.append([0, 0])
    ans = 1
    for i in range(n):
        if a[i] != a[i + 1]:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    l.sort()
    l.append([0, 0])
    count = 1
    for i in range(1, n + 1):
        if l[i - 1] != l[i]:
            count += 1
    print(count)

=======
Suggestion 7

def main():
    N = int(input())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    L.sort(key=lambda x: x[0])
    #print(L)
    ans = 0
    for i in range(N-1):
        if L[i] != L[i+1]:
            ans += 1
    print(ans+1)

=======
Suggestion 8

def solve():
    N = int(input())
    L = []
    for _ in range(N):
        L.append([int(x) for x in input().split()])
    L.sort(key=lambda x: x[1:])
    ans = 1
    for i in range(N-1):
        if L[i] != L[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    array = []
    for i in range(n):
        array.append(input().split())
    #print(array)
    array2 = []
    for i in range(n):
        array2.append(array[i][1:])
    #print(array2)
    array3 = []
    for i in range(n):
        array3.append(''.join(array2[i]))
    #print(array3)
    array4 = []
    for i in range(n):
        array4.append(int(array3[i]))
    #print(array4)
    array5 = []
    for i in range(n):
        array5.append(array4.count(array4[i]))
    #print(array5)
    array6 = []
    for i in range(n):
        if array5[i] == 1:
            array6.append(1)
        else:
            array6.append(0)
    #print(array6)
    print(sum(array6))

=======
Suggestion 10

def main():
    N = int(input())
    L = []
    for i in range(N):
        L.append(tuple(map(int, input().split())))

    L.sort(key=lambda x: x[0])
    #print(L)

    c = 0
    for i in range(N):
        #print("i", i)
        for j in range(i + 1, N):
            #print("j", j)
            if L[i][0] == L[j][0]:
                if L[i][1:] == L[j][1:]:
                    L[j] = ()
                else:
                    c += 1
            else:
                break

    #print(L)
    print(N - c)
