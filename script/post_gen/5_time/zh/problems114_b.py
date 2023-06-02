Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # input
    S = input()
    # solve
    min_diff = 1000
    for i in range(len(S)-2):
        X = int(S[i:i+3])
        diff = abs(X-753)
        if diff < min_diff:
            min_diff = diff
    # output
    print(min_diff)
    return

=======
Suggestion 2

def main():
    s = input()
    n = len(s)
    x = 753
    for i in range(n-2):
        x = min(x, abs(753-int(s[i:i+3])))
    print(x)

=======
Suggestion 3

def main():
    S = input()
    num = len(S)
    min_diff = 753
    for i in range(num-2):
        x = int(S[i:i+3])
        diff = abs(x-753)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

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

=======
Suggestion 5

def main():
    s = input()
    nums = []
    for i in range(3, len(s)):
        nums.append(int(s[i-3:i]))
    nums.sort()
    min_diff = 753 - nums[0]
    for i in range(1, len(nums)):
        diff = 753 - nums[i]
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 6

def main():
    s = input()
    min_diff = 1000
    for i in range(len(s) - 2):
        x = int(s[i:i+3])
        diff = abs(x - 753)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 7

def main():
    S = input()
    S = [int(i) for i in S]
    min_diff = 753 - int(''.join([str(i) for i in S[:3]]))
    for i in range(1, len(S) - 2):
        diff = 753 - int(''.join([str(i) for i in S[i:i+3]]))
        if abs(diff) < abs(min_diff):
            min_diff = diff
    print(abs(min_diff))

=======
Suggestion 8

def main():
    s = input()
    print(min(abs(int(s[i:i+3])-753) for i in range(len(s)-2)))

=======
Suggestion 9

def main():
    S = input()
    X = 0
    for i in range(0,len(S)-2):
        X = int(S[i:i+3])
        if abs(X-753) < abs(X-753-1):
            print(abs(X-753))
            break

=======
Suggestion 10

def get_min_diff(s):
    min_diff = 1000
    for i in range(len(s)-2):
        x = int(s[i:i+3])
        diff = abs(753 - x)
        if diff < min_diff:
            min_diff = diff
    return min_diff
