Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    d = {}
    for i in range(n):
        l = list(map(int, input().split()))
        l = tuple(l[1:])
        if l in d:
            d[l] += 1
        else:
            d[l] = 1
    print(len(d))

=======
Suggestion 2

def main():
    N = int(input())
    S = set()
    for i in range(N):
        L = list(map(int,input().split()))
        S.add(tuple(L[1:]))
    print(len(S))

=======
Suggestion 3

def main():
    N = int(input())
    L = []
    for i in range(N):
        L.append(input().split())
    for i in range(N):
        L[i][0] = int(L[i][0])
        for j in range(1,L[i][0]+1):
            L[i][j] = int(L[i][j])
    L.sort()
    ans = 1
    for i in range(1,N):
        if L[i-1][0] != L[i][0]:
            ans += 1
        else:
            for j in range(1,L[i][0]+1):
                if L[i-1][j] != L[i][j]:
                    ans += 1
                    break
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    dict = {}
    for i in range(N):
        L = list(map(int, input().split()))
        if L[0] in dict:
            dict[L[0]].append(L[1:])
        else:
            dict[L[0]] = [L[1:]]

    ans = 0
    for key in dict:
        ans += len(set([tuple(v) for v in dict[key]]))
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    d = dict()
    for i in range(N):
        L = list(map(int, input().split()))
        L = tuple(L[1:])
        d[L] = d.get(L, 0) + 1
    print(len(d))

=======
Suggestion 6

def main():
    N = int(input())
    A = [list(map(int, input().split())) for i in range(N)]

    d = {}
    for i in range(N):
        L = A[i][0]
        a = tuple(A[i][1:])
        if a in d:
            d[a] += 1
        else:
            d[a] = 1

    print(len(d))

=======
Suggestion 7

def main():
    N = int(input())
    A = []
    for i in range(N):
        L, *a = map(int, input().split())
        A.append(a)

    A.sort()
    ans = 0
    for i in range(N):
        if i == 0 or A[i - 1] != A[i]:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    #print(A)
    B = []
    for i in range(N):
        B.append(tuple(A[i][1:]))
    #print(B)
    ans = len(set(B))
    print(ans)
main()

=======
Suggestion 9

def main():
    N = int(input())
    L = []
    for i in range(N):
        L.append(tuple(map(int, input().split())))
    
    print(len(set(L)))

=======
Suggestion 10

def main():
    N = int(input())
    # N = 2 * 10 ** 5
    # N = 1
    # L = [1] * N
    # A = [[1] * L[i] for i in range(N)]
    L = []
    A = []
    for _ in range(N):
        l = list(map(int, input().split()))
        L.append(l[0])
        A.append(l[1:])
    # print(L)
    # print(A)
    # print(N, L, A)
    # print(len(A))
    # print(len(A[0]))
    # print(A[0][0])

    # 1. 重複している数列を削除
    # 2. 同じ数列を削除
    # 3. 重複している数列を削除
    # 4. 同じ数列を削除
    # 5. 重複している数列を削除
    # 6. 同じ数列を削除
    # 7. 重複している数列を削除
    # 8. 同じ数列を削除
    # 9. 重複している数列を削除
    # 10. 同じ数列を削除
    # 11. 重複している数列を削除
    # 12. 同じ数列を削除
    # 13. 重複している数列を削除
    # 14. 同じ数列を削除
    # 15. 重複している数列を削除
    # 16. 同じ数列を削除
    # 17. 重複している数列を削除
    # 18. 同じ数列を削除
    # 19. 重複している数列を削除
    # 20. 同じ数列を削除
    # 21. 重複している
