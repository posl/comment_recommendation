Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = set()
    for _ in range(n):
        s.add(input())
    print(len(s))

=======
Suggestion 2

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print(len(set(s)))

=======
Suggestion 3

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    print(len(set(s)))

=======
Suggestion 4

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    print(len(set(S)))

=======
Suggestion 5

def main():
    n = int(input())
    s = []
    for _ in range(n):
        s.append(input())
    print(len(set(s)))

=======
Suggestion 6

def main():
    n = int(input())
    s = [input() for i in range(n)]
    print(len(set(s)))

=======
Suggestion 7

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    ans = 0
    for i in range(N):
        if i == 0:
            ans += 1
        elif S[i] != S[i-1]:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    print(len(set(S)))
main()  # 出力結果: 実行時間制限超過

=======
Suggestion 9

def count_unique_elements(list):
    return len(set(list))

n = int(input())
s = [input() for i in range(n)]

print(count_unique_elements(s))
