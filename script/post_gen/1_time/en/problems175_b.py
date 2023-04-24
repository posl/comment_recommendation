Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[k] != L[i]:
                    if L[i] + L[j] > L[k]:
                        ans += 1
    print(ans)

main()

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
                if L[i] + L[j] > L[k]:
                    ans += 1
                else:
                    break
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    L = sorted(list(map(int, input().split())))
    ans = 0
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                if L[i] != L[j] and L[j] != L[k] and L[k] != L[i]:
                    if L[i] + L[j] > L[k]:
                        ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[k] != L[i]:
                    if L[i] + L[j] > L[k]:
                        count += 1
    print(count)

=======
Suggestion 5

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N - 2):
        a = L[i]
        for j in range(i + 1, N - 1):
            b = L[j]
            for k in range(j + 1, N):
                c = L[k]
                if a != b and b != c and c != a and a + b > c:
                    ans += 1
    print(ans)

=======
Suggestion 6

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
Suggestion 7

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort(reverse=True)
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if L[i] < L[j] + L[k]:
                    count += 1
    print(count)

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
                if L[i] != L[j] and L[j] != L[k] and L[k] != L[i]:
                    if L[i] + L[j] > L[k]:
                        ans += 1

    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    l = [int(x) for x in input().split()]
    l.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] + l[j] > l[k]:
                    ans += 1
    print(ans)

=======
Suggestion 10

def main():
    #N = int(input())
    #L = list(map(int, input().split()))
    N = 10
    L = [9, 4, 6, 1, 9, 6, 10, 6, 6, 8]
    L.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] < L[j] + L[k]:
                    ans += 1
    print(ans)
