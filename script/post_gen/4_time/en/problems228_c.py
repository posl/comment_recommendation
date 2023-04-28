Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    P = []
    for i in range(N):
        P.append(list(map(int, input().split())))
    for i in range(N):
        P[i].sort(reverse=True)
    for i in range(N):
        if P[i][0] + P[i][1] + P[i][2] + 1 + K * 3 > N:
            print('No')
        else:
            print('Yes')

=======
Suggestion 2

def solve():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P = [sum(p) for p in P]
    P.sort(reverse=True)
    print("Yes" if P[K - 1] > 0 else "No")
solve()

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    P = []
    for i in range(N):
        P.append(list(map(int, input().split())))
    P.sort(key=lambda x: x[0] + x[1] + x[2], reverse=True)
    print('Yes' if P[K-1][0] + P[K-1][1] + P[K-1][2] > 0 else 'No')

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for i in range(N)]
    R = [sum(P[i]) for i in range(N)]
    R.sort(reverse=True)
    print("Yes" if R[K-1] > R[K] else "No")

=======
Suggestion 5

def solve():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P.sort(key = lambda x: x[0]+x[1]+x[2], reverse = True)
    print('Yes' if sum([1 for i in range(K) if P[i][0]+P[i][1]+P[i][2] == P[K-1][0]+P[K-1][1]+P[K-1][2]]) == K else 'No')

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for i in range(N)]
    P_total = [sum(P[i]) for i in range(N)]
    P_total.sort(reverse=True)
    print('Yes' if P_total[K-1] == P_total[K] else 'No')

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    p_list = [list(map(int, input().split())) for _ in range(n)]
    for p in p_list:
        if sum(p) < k*3:
            print("Yes")
        else:
            print("No")

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    P = []
    for i in range(N):
        P.append(list(map(int, input().split())))
    #print(P)
    R = []
    for i in range(N):
        R.append(sum(P[i]))
    #print(R)
    R.sort(reverse=True)
    #print(R)
    for i in range(K):
        if R[i] < 300 * 4:
            print("Yes")
        else:
            print("No")

main()

=======
Suggestion 9

def rank(N, K, P):
    students = []
    for i in range(N):
        students.append(sum(P[i]))
    students.sort(reverse=True)
    if students[K-1] == students[K]:
        return 'No'
    else:
        return 'Yes'

N, K = map(int, input().split())
P = [list(map(int, input().split())) for i in range(N)]
print(rank(N, K, P))

=======
Suggestion 10

def exam(n, k, p):
  ans = 0
  for i in range(n):
    if sum(p[i]) >= 350:
      ans += 1
  return 'Yes' if ans >= k else 'No'

n, k = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(n)]
print(exam(n, k, p))
