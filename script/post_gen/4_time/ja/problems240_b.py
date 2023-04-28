Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(len(set(a)))

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 1
    for i in range(1, n):
        if a[i] != a[i - 1]:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    a_list = list(map(int, input().split()))
    a_set = set(a_list)
    print(len(a_set))
