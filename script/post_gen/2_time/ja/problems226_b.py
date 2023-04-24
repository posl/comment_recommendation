Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    D = {}
    for i in range(N):
        L, *A = map(int, input().split())
        A = tuple(A)
        if A in D:
            D[A] += 1
        else:
            D[A] = 1
    print(len(D))

=======
Suggestion 2

def main():
    N = int(input())
    d = {}
    for i in range(N):
        L = list(map(int, input().split()))
        L = tuple(L[1:])
        if L in d:
            d[L] += 1
        else:
            d[L] = 1
    print(len(d))

=======
Suggestion 3

def main():
    n = int(input())
    d = {}
    for i in range(n):
        l = list(map(int,input().split()))
        l = tuple(l[1:])
        if l in d:
            d[l] += 1
        else:
            d[l] = 1
    print(len(d))

=======
Suggestion 4

def main():
    N = int(input())
    D = {}
    for i in range(N):
        L, *A = map(int, input().split())
        if L not in D:
            D[L] = {}
        if tuple(A) not in D[L]:
            D[L][tuple(A)] = 0
        D[L][tuple(A)] += 1

    ans = 0
    for L in D:
        ans += len(D[L])
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    D = {}
    for i in range(N):
        L = list(map(int, input().split()))
        if L[0] not in D:
            D[L[0]] = [L[1:]]
        else:
            D[L[0]].append(L[1:])

    ans = 1
    for i in D:
        ans *= len(set(map(tuple, D[i])))
        ans %= 10**9 + 7
    print(ans)

=======
Suggestion 6

def solve(N, L, A):
    from collections import defaultdict
    d = defaultdict(int)
    for i in range(N):
        d[tuple(A[i])] += 1
    return len(d)

=======
Suggestion 7

def main():
    N = int(input())
    L = []
    for i in range(N):
        l = list(map(int, input().split()))
        L.append(l)

    L.sort()
    count = 1
    for i in range(N-1):
        if L[i] != L[i+1]:
            count += 1
    print(count)

=======
Suggestion 8

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))
    b = []
    for i in range(n):
        b.append(tuple(a[i][1::]))
    print(len(set(b)))

main()

=======
Suggestion 9

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    print(len(set(S)))

=======
Suggestion 10

def main():
    N = int(input())
    # 重複を許さないリスト
    # set()は重複を許さないリスト
    # set()は辞書型のように使える
    # set()は要素が順番に並んでいない
    # set()は要素の追加、削除ができる
    # set()は要素の重複を許さない
    # set()は要素の順番が保証されない
    # set()は要素の追加、削除ができる
    # set()は要素の重複を許さない
    # set()は要素の順番が保証されない
    # set()は要素の追加、削除ができる
    # set()は要素の重複を許さない
    # set()は要素の順番が保証されない
    # set()は要素の追加、削除ができる
    # set()は要素の重複を許さない
    # set()は要素の順番が保証されない
    # set()は要素の追加、削除ができる
    # set()は要素の重複を許さない
    # set()は要素の順番が保証されない
    # set()は要素の追加、削除ができる
    # set()は要素の重複を許さない
    # set()は要素の順番が保証されない
    # set()は要素の追加、削除ができる
    # set()は要素の重複を許さない
    # set()は要素の順番が保証されない
    # set()は要素の追加、削
