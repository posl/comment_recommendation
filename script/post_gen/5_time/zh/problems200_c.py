Synthesizing 10/10 solutions

=======
Suggestion 1

def count_pairs(arr):
    # Write your code here
    count = 0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if (arr[i]-arr[j])%200 == 0:
                count += 1
    return count

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = [0] * 200
    for i in range(n):
        count[a[i] % 200] += 1
    ans = 0
    for i in range(200):
        ans += count[i] * (count[i] - 1) // 2
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    #print(A)
    A200 = [i%200 for i in A]
    #print(A200)
    A200_dict = {}
    for i in A200:
        if i in A200_dict:
            A200_dict[i] += 1
        else:
            A200_dict[i] = 1
    #print(A200_dict)
    sum = 0
    for i in A200_dict.keys():
        sum += A200_dict[i]*(A200_dict[i]-1)//2
    print(sum)

=======
Suggestion 4

def problem200_c():
    N = int(input())
    A = list(map(int, input().split()))
    d = {}
    for a in A:
        mod = a % 200
        if mod in d:
            d[mod] += 1
        else:
            d[mod] = 1
    ans = 0
    for k in d:
        n = d[k]
        ans += n * (n - 1) // 2
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            if (A[i]-A[j])%200 == 0:
                count += 1
    print(count)

=======
Suggestion 6

def problems200_c():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a % 200 for a in A]
    a_mod = [0] * 200
    for a in A:
        a_mod[a] += 1
    ans = 0
    for i in range(200):
        ans += a_mod[i] * (a_mod[i] - 1) // 2
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int,input().split()))
    #print(N,A)
    #print(A)
    #print(len(A))
    count = 0
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            #print(i,j)
            if (A[i] - A[j]) % 200 == 0:
                count += 1
    print(count)

=======
Suggestion 8

def solution():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * 200
    for i in range(n):
        cnt[a[i] % 200] += 1
    ans = 0
    for i in range(200):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)

=======
Suggestion 9

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * 200
    for i in range(n):
        cnt[a[i] % 200] += 1
    ans = 0
    for i in range(200):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)

=======
Suggestion 10

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * 200
    for i in range(n):
        b[a[i] % 200] += 1
    ans = 0
    for i in range(200):
        ans += b[i] * (b[i] - 1) // 2
    print(ans)

solve()
