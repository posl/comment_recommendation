Synthesizing 10/10 solutions

=======
Suggestion 1

def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

=======
Suggestion 2

def main():
    N = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(2, 2 * 10 ** 5 + 1):
        d[i] = 0
    d[1] = 1
    count = 0
    for i in range(N):
        d[a[i]] += 1
        if d[a[i]] == 2:
            count -= 1
        if d[a[i] + 1] == 0:
            count += 1
        d[a[i] + 1] += 1
        print(count)
    return

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    l = [0] * (2 * 10**5 + 1)
    for i in range(n):
        l[a[i]] += 1
    ans = 0
    for i in range(2 * 10**5):
        ans = max(ans, l[i] + l[i + 1] + l[i + 2])
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    s = [0] * (2 * 10 ** 5 + 1)
    for i in range(n):
        s[a[i]] += 1
    ans = 0
    for i in range(2 * 10 ** 5 + 1):
        ans += s[i] * (s[i] - 1) // 2
    for i in range(n):
        print(ans - s[a[i]] + 1)

=======
Suggestion 5

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    cnt = {}
    for a in A:
        cnt[a] = cnt.get(a, 0) + 1
    for i in range(1, 200001):
        if i not in cnt:
            continue
        if cnt[i] == 1:
            ans[A.index(i)] = 1
        else:
            ans[A.index(i)] = 0
        for j in range(2 * i, 200001, i):
            if j not in cnt:
                continue
            if cnt[j] == 1:
                ans[A.index(i)] += 1
            cnt[j] = 0
    for i in ans:
        print(i)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(n, a)
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    #print(d)
    count = 0
    for k, v in d.items():
        if v >= k:
            count += v - k
        else:
            count += v
    print(count)

=======
Suggestion 7

def main():
    N = int(input())
    a_list = [int(x) for x in input().split()]

    a_dict = {}
    for i in range(len(a_list)):
        if a_list[i] in a_dict:
            a_dict[a_list[i]] += 1
        else:
            a_dict[a_list[i]] = 1

    ans_list = []
    ans_list.append(len(a_dict))
    for i in range(1, len(a_list)):
        if a_list[i-1] in a_dict:
            a_dict[a_list[i-1]] -= 1
            if a_dict[a_list[i-1]] == 0:
                del a_dict[a_list[i-1]]
        ans_list.append(len(a_dict))

    for i in range(len(ans_list)):
        print(ans_list[i])

=======
Suggestion 8

def main():
  n = int(input())
  a = list(map(int, input().split()))
  ans = [0] * n
  for i in range(n):
    ans[i] = a[i]
  for i in range(1, n):
    if ans[i-1] == a[i]:
      ans[i] = 0
      ans[i-1] = 0
  ans = [i for i in ans if i != 0]
  print(len(ans))

=======
Suggestion 9

def solve(n, a):
    ans = [0] * n
    from collections import defaultdict
    d = defaultdict(int)
    for i in range(n):
        ans[i] = i - d[a[i]]
        d[a[i]] += 1
    return ans

n = int(input())
a = list(map(int, input().split()))
print(*solve(n, a), sep='\n')

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.reverse()
    balls = set()
    for i in range(N):
        if i == 0:
            balls.add(A[i])
        else:
            if A[i] in balls:
                balls.remove(A[i])
            else:
                balls.add(A[i])
    print(len(balls))
