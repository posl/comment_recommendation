Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_input():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    return n, t, a, h

=======
Suggestion 2

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    diff = [abs(A - (T - h * 0.006)) for h in H]
    print(diff.index(min(diff)) + 1)

=======
Suggestion 3

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    h = [abs(t - i * 0.006 - a) for i in h]
    print(h.index(min(h)) + 1)

=======
Suggestion 4

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    print(min(range(N), key=lambda i:abs(A-(T-H[i]*0.006)))+1)

=======
Suggestion 5

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    H = [T - h * 0.006 for h in H]
    diff = [abs(A - h) for h in H]
    print(diff.index(min(diff)) + 1)

=======
Suggestion 6

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    min = 100000
    for i in range(N):
        if abs(T - H[i] * 0.006 - A) < min:
            min = abs(T - H[i] * 0.006 - A)
            ans = i + 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    temp = 10**9
    for i in range(N):
        if abs(T - H[i] * 0.006 - A) < temp:
            ans = i + 1
            temp = abs(T - H[i] * 0.006 - A)
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    T,A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    min = 1000000
    for i in range(N):
        if abs(A - (T - H[i] * 0.006)) < min:
            min = abs(A - (T - H[i] * 0.006))
            ans = i + 1
    print(ans)

=======
Suggestion 9

def calc_temp(t, h):
    return abs(t - h * 0.006)

N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

temp_list = list(map(lambda x: calc_temp(T, x), H))

print(temp_list.index(min(temp_list)) + 1)
