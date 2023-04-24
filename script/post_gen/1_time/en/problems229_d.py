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
            max_count = max(max_count, count)
            count = 0
    max_count = max(max_count, count)
    print(min(max_count + K, len(S)))

=======
Suggestion 2

def max_consecutive_x(s, k):
    max_consecutive_x = 0
    consecutive_x = 0
    for i in range(len(s)):
        if s[i] == 'X':
            consecutive_x += 1
        else:
            if k > 0:
                consecutive_x += 1
                k -= 1
            else:
                consecutive_x = 0
        if consecutive_x > max_consecutive_x:
            max_consecutive_x = consecutive_x
    return max_consecutive_x

=======
Suggestion 3

def main():
    S = input()
    K = int(input())
    S = S.replace('.', ' ')
    S = S.split()
    if len(S) == 1:
        print(len(S[0]))
    elif len(S) == 0:
        print(0)
    else:
        count = 0
        for i in range(len(S)):
            count += len(S[i])
        count += K - 1
        print(count)

=======
Suggestion 4

def main():
    S = input()
    K = int(input())
    S = S.replace('.', ' ')
    S = S.split()
    ans = 0
    for i in range(len(S)):
        ans += len(S[i])
    ans -= K
    ans = max(ans, 0)
    print(ans)

=======
Suggestion 5

def main():
    s = input()
    k = int(input())
    n = len(s)
    if k == 0:
        print(max(map(len, s.split('.'))))
        return
    if n == 1:
        print(1)
        return
    if s[0] == 'X':
        s = '.' + s
    if s[-1] == 'X':
        s = s + '.'
    s = s.replace('X', '.')
    s = s.replace('..', '.')
    if s[0] == '.':
        s = s[1:]
    if s[-1] == '.':
        s = s[:-1]
    if len(s) == 0:
        print(0)
        return
    if k >= len(s):
        print(len(s))
        return
    s = s.split('.')
    if k == len(s):
        print(sum(map(len, s)) + k - 1)
        return
    if k < len(s):
        print(sum(map(len, s[:k + 1])) + k)
        return

=======
Suggestion 6

def main():
    # input
    S = input()
    K = int(input())

    # compute

    # output
    print(max([len(s) for s in S.replace('.', ' ').split()]))

=======
Suggestion 7

def main():
    s = input()
    k = int(input())
    s = s.replace('.', ' ')
    s = s.split()
    x = []
    for i in s:
        x.append(len(i))
    x.sort()
    x.reverse()
    print(x[0] + k)

=======
Suggestion 8

def main():
    s = input()
    k = int(input())
    x = s.split('.')
    y = [len(i) for i in x]
    y.sort(reverse=True)
    print(y[0]-k if y[0]-k>0 else 0)

=======
Suggestion 9

def get_input():
    s = input()
    k = int(input())
    return s, k

=======
Suggestion 10

def main():
    S = input()
    K = int(input())
    print(solution(S, K))
