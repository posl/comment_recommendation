Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N//2):
        if A[i] != A[N-1-i]:
            cnt += 1
    print(cnt)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n//2):
        if a[i] != a[n-i-1]:
            cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N//2):
        if A[i] != A[-1-i]:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_max = max(a)
    a_min = min(a)
    if a_max == a_min:
        print(0)
        return
    a_max_count = a.count(a_max)
    a_min_count = a.count(a_min)
    if (a_max_count + a_min_count) == n:
        print(1)
        return
    a_max_index = a.index(a_max)
    a_min_index = a.index(a_min)
    if a_max_index < a_min_index:
        if a_max_count > a_min_count:
            print(n - a_max_count)
        else:
            print(n - a_min_count)
    else:
        if a_max_count > a_min_count:
            print(n - a_min_count)
        else:
            print(n - a_max_count)

=======
Suggestion 5

def make_palindrome(a):
    if len(a) == 1:
        return 0
    if len(a) == 2:
        if a[0] == a[1]:
            return 0
        else:
            return 1
    a.sort()
    count = 0
    i = 0
    j = len(a) - 1
    while i < j:
        if a[i] == a[j]:
            i += 1
            j -= 1
        elif a[i] < a[j]:
            a[i+1] = a[i] + a[i+1]
            count += 1
            i += 1
        else:
            a[j-1] = a[j] + a[j-1]
            count += 1
            j -= 1
    return count

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = max(a)
    c = [0] * (m + 1)
    for i in a:
        c[i] += 1
    if c.count(0) == m + 1:
        print(0)
        return
    print(n - max(c))

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(set(a))
    c = 0
    for i in range(len(b)):
        c = max(c, a.count(b[i]))
    print(n-c)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_set = set(a)
    a_dict = {}
    for i in a_set:
        a_dict[i] = a.count(i)
    a_dict = sorted(a_dict.items(), key=lambda x:x[1], reverse=True)
    if len(a) == 1:
        print(0)
    elif len(a) == 2:
        if a[0] == a[1]:
            print(0)
        else:
            print(1)
    elif len(a_set) == 1:
        print(0)
    else:
        if a_dict[0][1] == 1:
            print(1)
        else:
            if a_dict[0][1] == 2:
                if a_dict[1][1] == 1:
                    print(1)
                else:
                    print(2)
            else:
                if a_dict[1][1] == 1:
                    print(2)
                else:
                    print(3)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_set = set(A)
    if len(A) == len(A_set):
        print(0)
        return
    A_dict = {}
    for a in A:
        if a in A_dict:
            A_dict[a] += 1
        else:
            A_dict[a] = 1
    A_dict = sorted(A_dict.items(), key=lambda x:x[1], reverse=True)
    print(N - A_dict[0][1])
