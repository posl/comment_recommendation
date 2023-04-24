Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    n = int(input())
    d = {}
    for i in range(n):
        s = input()
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    print(max(d, key=d.get))

=======
Suggestion 2

def main():
    N = int(input())
    S = [input() for i in range(N)]
    print(max(S, key=S.count))

=======
Suggestion 3

def main():
    n = int(input())
    s = [input() for i in range(n)]
    print(max(set(s), key=s.count))

=======
Suggestion 4

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    print(max(set(S), key=S.count))

=======
Suggestion 5

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    print(max(S, key=lambda x: S.count(x)))

=======
Suggestion 6

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    s.reverse()
    print(s[0])

=======
Suggestion 7

def main():
    N = int(input())
    S = [input() for i in range(N)]

    print(max(set(S), key = S.count))

=======
Suggestion 8

def main():
    num = int(input())
    input_list = []
    for i in range(num):
        input_list.append(input())
    print(max(set(input_list), key=input_list.count))

=======
Suggestion 9

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    S.append("")
    max = 0
    max_name = ""
    current_count = 0
    current_name = ""
    for i in range(N + 1):
        if current_name != S[i]:
            if current_count > max:
                max = current_count
                max_name = current_name
            current_name = S[i]
            current_count = 1
        else:
            current_count += 1
    print(max_name)
main()
