Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    print(min(s.count('0'), s.count('1')) * 2)

=======
Suggestion 2

def main():
    S = input()
    print(min(S.count('0'), S.count('1')) * 2)

=======
Suggestion 3

def main():
    #input
    S = input()
    #compute
    cnt = 0
    for i in range(len(S)-1):
        if S[i] != S[i+1]:
            cnt += 1
    #output
    print(cnt)
    return 0

=======
Suggestion 4

def main():
    S = input()
    print(min(S.count("0"), S.count("1")) * 2)

=======
Suggestion 5

def main():
    # input
    S = input()
    N = len(S)

    # compute

    # output
    print(min(S.count('0'), S.count('1'))*2)

=======
Suggestion 6

def main():
    input = input()
    print(input.count('0')*2 if input.count('0')*2 < len(input) else len(input))

main()

=======
Suggestion 7

def get_input():
    return input()
