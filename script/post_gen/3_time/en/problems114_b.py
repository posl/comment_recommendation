Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    N = len(S)
    ans = 999
    for i in range(N-2):
        ans = min(ans, abs(753 - int(S[i:i+3])))
    print(ans)

=======
Suggestion 2

def main():
    s = input()
    print(min(abs(int(s[i:i+3]) - 753) for i in range(len(s) - 2)))

=======
Suggestion 3

def main():
    S = input()
    min = 999
    for i in range(len(S)-2):
        X = int(S[i:i+3])
        if abs(X-753)<min:
            min = abs(X-753)
    print(min)
main()

=======
Suggestion 4

def lunlun(n):
    if n < 10:
        return n
    last_digit = n % 10
    if last_digit == 0:
        return lunlun(n - 1)
    elif last_digit == 9:
        return lunlun(n + 1)
    else:
        return lunlun(n - 1) if last_digit > n // 10 % 10 else lunlun(n + 1)

print(lunlun(int(input())))

=======
Suggestion 5

def main():
    S = input()
    result = 0
    for i in range(len(S)-2):
        temp = abs(753 - int(S[i:i+3]))
        if result == 0:
            result = temp
        elif temp < result:
            result = temp
    print(result)

=======
Suggestion 6

def main():
    S = input()
    x = 753
    for i in range(len(S)-2):
        x = min(x, abs(int(S[i:i+3])-753))
    print(x)

=======
Suggestion 7

def main():
    S = input()
    abs_min = 753
    for i in range(len(S)-2):
        abs_min = min(abs_min, abs(int(S[i:i+3])-753))
    print(abs_min)

=======
Suggestion 8

def main():
    #input
    S = input()

    #compute

    #output
    print('')

=======
Suggestion 9

def main():
    S = input()
    S = S + '0'
    L = len(S)
    ans = 1000

    for i in range(L-2):
        x = int(S[i:i+3])
        ans = min(ans, abs(753 - x))

    print(ans)

=======
Suggestion 10

def main():
    S = input()
    S = int(S)
    S = str(S)
    S = S.zfill(10)
    S = list(S)
    S = [int(s) for s in S]
    S = sorted(S)
    S = [str(s) for s in S]
    S = ''.join(S)
    S = int(S)
    if S < 753:
        print(753 - S)
    elif S >= 753:
        print(S - 753)
