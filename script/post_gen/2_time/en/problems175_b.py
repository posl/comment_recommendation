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
                if L[i] == L[j] or L[j] == L[k]:
                    continue
                if L[i] + L[j] > L[k]:
                    ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
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
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                if L[i] != L[j] and L[j] != L[k] and L[i] != L[k]:
                    if L[i] + L[j] > L[k]:
                        ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                if L[i] != L[j] and L[j] != L[k] and L[i] + L[j] > L[k]:
                    ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if l[i] != l[j] and l[j] != l[k] and l[k] < l[i] + l[j]:
                    ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] + l[j] > l[k]:
                    count += 1
                else:
                    break
    print(count)

=======
Suggestion 7

def main():
    N = int(input())
    L = list(map(int, input().split()))

    L.sort()

    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] != L[j] != L[k] and L[i] + L[j] > L[k]:
                    ans += 1

    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    L = list(map(int, input().split()))

    L.sort()

    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if L[i] != L[j] and L[j] != L[k] and L[k] != L[i]:
                    if L[i] + L[j] > L[k] and L[j] + L[k] > L[i] and L[k] + L[i] > L[j]:
                        ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    L = list(map(int, input().split()))

    L.sort()
    ans = 0

    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if L[i] == L[j] or L[i] == L[k] or L[j] == L[k]:
                    continue
                if L[i] + L[j] > L[k]:
                    ans += 1

    print(ans)

=======
Suggestion 10

def find_ways_to_make_triangles(stick_lengths):
    stick_lengths.sort()
    ways = 0
    for i in range(len(stick_lengths)):
        for j in range(i + 1, len(stick_lengths)):
            for k in range(j + 1, len(stick_lengths)):
                if stick_lengths[i] + stick_lengths[j] > stick_lengths[k]:
                    ways += 1
    return ways
