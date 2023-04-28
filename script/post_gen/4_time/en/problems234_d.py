Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(N-K+1):
        print(sorted(P[i:i+K])[-1])

=======
Suggestion 2

def main():
    N,K = map(int,input().split())
    P = list(map(int,input().split()))
    ans = []
    for i in range(N-K+1):
        ans.append(sorted(P[i:i+K])[-1])
    print(*ans, sep='\n')

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    ans = []
    for i in range(k-1, n):
        ans.append(sorted(p[:i+1])[k-1])
    print(*ans, sep='\n')

=======
Suggestion 4

def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k,n):
        if a[i-k] < a[i]:
            print("Yes")
        else:
            print("No")

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    ans = []
    ans.append(max(p[:k]))
    for i in range(k, n):
        if p[i] > ans[-1]:
            ans.append(p[i])
        else:
            ans.append(ans[-1])
    for i in range(len(ans)):
        print(ans[i])

=======
Suggestion 6

def main():
    n,k = map(int, input().split())
    p = list(map(int, input().split()))
    for i in range(n-k):
        if p[i] > p[i+k]:
            print("Yes")
        else:
            print("No")

=======
Suggestion 7

def main():
    n,k=map(int,input().split())
    p=list(map(int,input().split()))
    ans=[]
    for i in range(k,n+1):
        ans.append(sorted(p[0:i])[-k])
    for i in ans:
        print(i)

=======
Suggestion 8

def get_max(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

=======
Suggestion 9

def get_kth_greatest_value_of_first_i_terms_of_p(p, k, i):
    return sorted(p[:i], reverse=True)[k-1]

=======
Suggestion 10

def find_kth_greatest_value(P, K):
    P = sorted(P)
    return P[-K]
