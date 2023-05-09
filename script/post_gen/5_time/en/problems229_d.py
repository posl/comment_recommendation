Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    K = int(input())
    count = 0
    max_count = 0
    for i in range(len(S)):
        if S[i] == 'X':
            count += 1
        else:
            count = 0
        if count > max_count:
            max_count = count
    print(min(max_count+K, len(S)))

=======
Suggestion 2

def main():
    S = input()
    K = int(input())
    count = 0
    if S[0] == 'X':
        count = 1
    for i in range(1, len(S)):
        if S[i] == 'X':
            if S[i-1] == 'X':
                count += 1
            else:
                count = 1
        else:
            if count > 0:
                if K > 0:
                    count += 1
                    K -= 1
                else:
                    count = 0
    print(count)
main()

=======
Suggestion 3

def main():
    s = input()
    k = int(input())
    s = s.replace('X', 'X.')
    s = s.replace('..', '.')
    s = s.replace('X.', 'X')
    s = s.replace('..', '.')
    s = s.replace('X.', 'X')
    s = s.replace('..', '.')
    print(len(s) - 1)

=======
Suggestion 4

def main():
    s = input()
    k = int(input())
    s = s.replace('.', ' ')
    s = s.split()
    ans = 0
    for i in s:
        ans += len(i) - k
    print(ans)

=======
Suggestion 5

def main():
    s = input()
    k = int(input())
    s = s.replace('.', ',')
    s = s.split(',')
    s = [len(i) for i in s]
    s = [i-k for i in s]
    s = [i for i in s if i>0]
    s = [i+k for i in s]
    print(max(s))

=======
Suggestion 6

def main():
    S = input()
    K = int(input())
    S = S.replace(".", " ")
    S = S.split()
    S = "".join(S)
    S = S.split("X")
    S = [len(s) for s in S]
    S.sort(reverse=True)
    print(min(S[0] + K, len(S)))

=======
Suggestion 7

def main():
    S = input()
    K = int(input())
    S = S.replace('..', '.')
    S = S.replace('X', ' ')
    S = S.split(' ')
    S = [len(x) for x in S]
    S = [x for x in S if x > 0]
    S = [x + 1 for x in S]
    S = [0] + S + [0]
    ans = 0
    for i in range(len(S) - K - 1):
        ans = max(ans, sum(S[i:i + K + 1]))
    print(ans)

=======
Suggestion 8

def main():
    S = input()
    K = int(input())
    S = S.replace('.', ' ').split()
    S = [len(s) for s in S]
    S = [max(s - 2 * K, 0) for s in S]
    print(max(S))

=======
Suggestion 9

def main():
    S = input()
    K = int(input())
    S = S.replace('X','.')
    S = S.split('.')
    S = list(map(len, S))
    S = list(map(lambda x: x - 1, S))
    for i in range(len(S)):
        if K > 0:
            if S[i] > 0:
                if K >= S[i]:
                    K -= S[i]
                    S[i] += 1
                else:
                    S[i] += K
                    K = 0
    print(max(S))

=======
Suggestion 10

def main():
    S = input()
    K = int(input())
    T = S.replace('.', ' ')
    T = T.split()
    L = []
    for x in T:
        if len(x) >= K:
            L.append(len(x))
    if len(L) == 0:
        print(0)
    else:
        print(max(L))
