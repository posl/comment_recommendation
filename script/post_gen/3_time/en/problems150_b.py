Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    count = 0
    for i in range(n-2):
        if s[i:i+3] == 'ABC':
            count += 1
    print(count)

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    count = 0
    for i in range(n-2):
        if s[i:i+3] == "ABC":
            count += 1
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    ans = 0
    for i in range(n-2):
        if s[i:i+3] == 'ABC':
            ans += 1
    print(ans)

main()

=======
Suggestion 4

def countABC(S):
    count = 0
    for i in range(len(S) - 2):
        if S[i:i+3] == 'ABC':
            count += 1
    return count

=======
Suggestion 5

def main():
    import sys
    N = int(sys.stdin.readline())
    S = sys.stdin.readline().rstrip()
    count = 0
    for i in range(N-2):
        if S[i:i+3] == 'ABC':
            count += 1
    print(count)

=======
Suggestion 6

def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    S = input().rstrip()

    ans = 0
    for i in range(N-2):
        if S[i:i+3] == 'ABC':
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    print(S.count('ABC'))

main()

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    print(S.count('ABC'))

=======
Suggestion 9

def main():
    N = int(input())
    S = input()
    print(S.count("ABC"))
