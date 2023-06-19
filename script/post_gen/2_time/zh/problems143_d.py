Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()

    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] + l[j] > l[k]:
                    ans += 1
    print(ans)

=======
Suggestion 2

def triangle(n, l):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                a = l[i]
                b = l[j]
                c = l[k]
                if a < b + c and b < c + a and c < a + b:
                    count += 1
    return count

=======
Suggestion 3

def isTriangle(a, b, c):
    if a < b + c and b < c + a and c < a + b:
        return True
    return False

=======
Suggestion 4

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] + l[j] > l[k]:
                    cnt += 1
    print(cnt)

=======
Suggestion 5

def triangle_count(n, l):
    l.sort()
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if l[i] + l[j] > l[k]:
                    count += 1
                else:
                    break
    return count

=======
Suggestion 6

def triangle_num(num_list):
    num_list.sort()
    num_list.reverse()
    #print(num_list)
    count = 0
    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            for k in range(j+1, len(num_list)):
                if num_list[i] < num_list[j] + num_list[k]:
                    count += 1
                else:
                    break
    return count

=======
Suggestion 7

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if l[i] + l[j] > l[k]:
                    ans += 1
                else:
                    break
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] + L[j] > L[k] and L[j] + L[k] > L[i] and L[k] + L[i] > L[j]:
                    ans += 1
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    l = list(map(int, input().split()))

    l.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] + l[j] > l[k] and l[j] + l[k] > l[i] and l[k] + l[i] > l[j]:
                    ans += 1
    print(ans)
