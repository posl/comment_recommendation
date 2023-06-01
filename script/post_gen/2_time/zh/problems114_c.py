Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    min_diff = 1000
    for i in range(len(s)-2):
        x = int(s[i:i+3])
        if abs(x-753) < min_diff:
            min_diff = abs(x-753)
    print(min_diff)
main()

=======
Suggestion 2

def main():
    s = input()
    s = '0' + s
    ans = 1000
    for i in range(1, len(s) - 2):
        x = int(s[i:i + 3])
        ans = min(ans, abs(x - 753))
    print(ans)

=======
Suggestion 3

def get_min_diff(s):
    min_diff = 999
    for i in range(len(s)-2):
        num = int(s[i:i+3])
        diff = abs(num - 753)
        if diff < min_diff:
            min_diff = diff
    return min_diff

=======
Suggestion 4

def main():
    s = input()
    n = len(s)
    ans = 1000
    for i in range(n-2):
        x = int(s[i:i+3])
        ans = min(ans, abs(x-753))
    print(ans)
main()

=======
Suggestion 5

def main():
    s = input()
    min = 999
    for i in range(len(s)-2):
        a = int(s[i:i+3])
        if abs(a-753) < min:
            min = abs(a-753)
    print(min)

=======
Suggestion 6

def main():
    s = input()
    print(min(abs(int(s[i:i+3])-753) for i in range(len(s)-2)))

=======
Suggestion 7

def get_min_diff(s):
    min_diff = 753 - int(s[:3])
    for i in range(len(s)-2):
        temp = abs(int(s[i:i+3]) - 753)
        if temp < min_diff:
            min_diff = temp
    return min_diff

=======
Suggestion 8

def main():
    S = input()
    N = len(S)
    min_753 = 753
    for i in range(N-2):
        X = int(S[i:i+3])
        if abs(X-753) < min_753:
            min_753 = abs(X-753)
    print(min_753)

=======
Suggestion 9

def main():
    s = input()
    x = 0
    for i in range(4, len(s)+1):
        for j in range(len(s)-i+1):
            x = int(s[j:j+i])
            if abs(x-753) < abs(x-753):
                x = abs(x-753)
    print(x)

=======
Suggestion 10

def main():
    S = input()
    min_diff = 1000
    for i in range(len(S)-2):
        X = int(S[i:i+3])
        diff = abs(753 - X)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)
