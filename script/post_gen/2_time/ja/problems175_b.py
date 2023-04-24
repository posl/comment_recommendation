Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[k] < L[i] + L[j]:
                    ans += 1
    print(ans)
    return

=======
Suggestion 2

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[k] != L[i]:
                    if L[i] + L[j] > L[k]:
                        ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[k] < L[i] + L[j]:
                    ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort(reverse=True)
    cnt = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if L[i] < L[j] + L[k]:
                    cnt += 1
    print(cnt)

=======
Suggestion 5

def solve(n, l):
    l.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] != l[j] and l[j] != l[k] and l[i] != l[k] and l[i] + l[j] > l[k]:
                    ans += 1
    return ans

=======
Suggestion 6

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort(reverse=True)
    #print(L)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] < L[j] + L[k]:
                    ans += 1
                    #print(i, j, k)
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()

    # 三角形を作ることのできるような、長さの異なる 3 本の棒を選ぶ方法の個数を出力せよ。
    # 1 ≦ i < j < k ≦ N の組であって、L_i, L_j, L_k がすべて異なり、
    # 3 辺の長さが L_i, L_j, L_k であるような三角形が存在する
    # 1 ≦ i < j < k ≦ N の組であって、L_i, L_j, L_k がすべて異なる
    # 3 辺の長さが L_i, L_j, L_k であるような三角形が存在する
    # 1 ≦ i < j < k ≦ N の組であって、L_i, L_j, L_k がすべて異なる
    # 3 辺の長さが L_i, L_j, L_k であるような三角形が存在する
    # 1 ≦ i < j < k ≦ N の組であって、L_i, L_j, L_k がすべて異なる
    # 3 辺の長さが L_i, L_j, L_k であるような三角形が存在する
    # 1 ≦ i < j < k ≦ N の組であって、L_i, L_j, L_k がすべて異なる
    # 3 辺の長さが L_i, L_j, L_k であるような三角形が存在する
    # 1 ≦ i < j < k ≦ N の組であって、L_i, L_j, L_k がすべて異なる
    # 3 辺の長さが L_i, L_j, L_k で

=======
Suggestion 8

def main():
    N = int(input())
    L = list(map(int, input().split()))
    #L.sort(reverse=True)
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] == L[j] or L[j] == L[k] or L[k] == L[i]:
                    continue
                if L[i] + L[j] > L[k] and L[j] + L[k] > L[i] and L[k] + L[i] > L[j]:
                    count += 1
    print(count)
