Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    d = {}
    for i in range(N):
        a = list(map(int, input().split()))
        if a[0] in d:
            d[a[0]].append(a[1:])
        else:
            d[a[0]] = [a[1:]]
    ans = 1
    for i in d:
        ans *= len(set(map(tuple, d[i])))
    print(ans % (10**9 + 7))

=======
Suggestion 2

def main():
    N = int(input())
    d = {}
    for i in range(N):
        a = list(map(int, input().split()))
        a = tuple(a[1:])
        if a in d:
            d[a] += 1
        else:
            d[a] = 1
    print(len(d))

=======
Suggestion 3

def main():
    N = int(input())
    dic = {}
    for i in range(N):
        L = list(map(int, input().split()))
        if L[0] in dic:
            dic[L[0]].append(L[1:])
        else:
            dic[L[0]] = [L[1:]]
    count = 0
    for i in dic:
        count += len(set(map(tuple, dic[i])))
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    D = {}
    for i in range(N):
        L = list(map(int, input().split()))
        if L[0] in D:
            D[L[0]].append(L[1:])
        else:
            D[L[0]] = [L[1:]]
    ans = 0
    for key in D:
        ans += len(set(map(tuple, D[key])))
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    D = set()
    for i in range(N):
        L, *A = map(int, input().split())
        D.add((L, tuple(A)))
    print(len(D))

=======
Suggestion 6

def main():
    n = int(input())
    ans = 0
    d = {}
    for _ in range(n):
        l = list(map(int, input().split()))
        l = l[1:]
        if tuple(l) in d:
            d[tuple(l)] += 1
        else:
            d[tuple(l)] = 1
    print(len(d))
    return

=======
Suggestion 7

def main():
    N = int(input())
    print(len(set(tuple(map(int, input().split()))[1:] for _ in range(N))))

=======
Suggestion 8

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    #print(A)
    ans = N
    for i in range(N):
        for j in range(1, A[i][0]+1):
            if A[i][j] == 1:
                ans -= 1
                break
    print(ans)

main()

=======
Suggestion 9

def main():
    N = int(input())
    seq = []
    for i in range(N):
        seq.append(input().split())
    seq.sort(key=lambda x: x[0])
    seq.sort(key=lambda x: x[1:])
    ans = 1
    for i in range(1, N):
        if seq[i-1] != seq[i]:
            ans += 1
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    count = 0
    d = {}
    for i in range(N):
        #print(i)
        s = input().split()
        #print(s)
        s = s[1:]
        #print(s)
        s = ' '.join(s)
        #print(s)
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    print(len(d))
