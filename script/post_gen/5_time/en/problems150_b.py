Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    count = 0
    for i in range(n-2):
        if s[i:i+3] == "ABC":
            count += 1
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N-2):
        if S[i:i+3] == 'ABC':
            count += 1
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    cnt = 0
    for i in range(n-2):
        if s[i:i+3] == "ABC":
            cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    ans = 0
    for i in range(N-2):
        if S[i:i+3] == "ABC":
            ans += 1
    print(ans)

=======
Suggestion 5

def problems150_b():
    N = int(input())
    S = input()
    count = 0
    for i in range(N-2):
        if S[i] == "A" and S[i+1] == "B" and S[i+2] == "C":
            count += 1
    print(count)

=======
Suggestion 6

def solve():
    N = int(input())
    S = input()
    res = 0
    for i in range(N-2):
        if S[i:i+3] == "ABC":
            res += 1
    print(res)

=======
Suggestion 7

def count_substring(string, sub_string):
    count = 0
    for i in range(0,len(string)-len(sub_string)+1):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count

N = int(input())
S = input()
print(count_substring(S, 'ABC'))

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    print(s.count("ABC"))
