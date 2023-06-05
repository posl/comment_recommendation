Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    print(len(set(tuple(l) for l in L)))

=======
Suggestion 2

def main():
    n = int(input())
    seqs = {}
    for i in range(n):
        seq = tuple(map(int, input().split()[1:]))
        if seq not in seqs:
            seqs[seq] = 1
        else:
            seqs[seq] += 1
    print(len(seqs))

=======
Suggestion 3

def main():
    n = int(input())
    d = {}
    for i in range(n):
        tmp = tuple(map(int, input().split()))
        if tmp in d:
            d[tmp] += 1
        else:
            d[tmp] = 1
    print(len(d))

=======
Suggestion 4

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append([int(x) for x in input().split()][1:])
    a.sort()
    ans = 1
    for i in range(n - 1):
        if a[i] != a[i + 1]:
            ans += 1
    print(ans)

main()

=======
Suggestion 5

def main():
    N = int(input())
    L = []
    for i in range(N):
        L.append(input().split())
    L = [int(L[i][0]) for i in range(N)]
    print(len(set(L)))

=======
Suggestion 6

def main():
    n = int(input())
    result = set()
    for i in range(n):
        line = input().split()
        result.add(tuple(line[1:]))
    print(len(result))

=======
Suggestion 7

def main():
    n = int(input())
    seq = []
    for i in range(n):
        seq.append(input().split())
    print(len(set(map(tuple,seq))))

=======
Suggestion 8

def main():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    a = [tuple(a[i][1:]) for i in range(n)]
    print(len(set(a)))

=======
Suggestion 9

def main():
    n = int(input())
    num = []
    for i in range(n):
        num.append(input().split())

    for i in range(n):
        num[i][0] = int(num[i][0])
        for j in range(num[i][0]):
            num[i][j+1] = int(num[i][j+1])

    num.sort(key=lambda x: x[1:])

    count = 1
    for i in range(n-1):
        if num[i] != num[i+1]:
            count += 1

    print(count)

=======
Suggestion 10

def main():
    N = int(input())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))

    L.sort(key=lambda x:x[0])
    #print(L)
    cnt = 1
    for i in range(N-1):
        if L[i] == L[i+1]:
            continue
        else:
            cnt += 1
    print(cnt)
