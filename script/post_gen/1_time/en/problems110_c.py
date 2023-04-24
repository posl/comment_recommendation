Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    s_set = set(s)
    t_set = set(t)
    if len(s_set) == len(t_set):
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    S = input()
    T = input()
    s = set(S)
    t = set(T)
    if len(s) == len(t):
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    S = input()
    T = input()
    if len(set(S)) == len(set(T)):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if len(set(S)) == len(set(T)):
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    S = list(input())
    T = list(input())
    S = sorted(S)
    T = sorted(T, reverse = True)
    if S < T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    s = input()
    t = input()

    if len(set(s)) < len(set(t)):
        print("No")
    else:
        print("Yes")

=======
Suggestion 7

def main():
    S = input()
    T = input()
    S = sorted(S)
    T = sorted(T, reverse=True)
    print('Yes' if S < T else 'No')

=======
Suggestion 8

def main():
    S = input()
    T = input()
    pairs = []
    for i in range(len(S)):
        pairs.append([S[i], T[i]])
    pairs.sort()
    for i in range(len(pairs)-1):
        if pairs[i][0] == pairs[i+1][0] and pairs[i][1] != pairs[i+1][1]:
            print('No')
            return
    print('Yes')

=======
Suggestion 9

def main():
    S = input()
    T = input()

    # Check if the number of distinct characters in S and T are the same
    if len(set(S)) == len(set(T)):
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    S = input()
    T = input()

    # 1. Check if |S| = |T|
    if len(S) != len(T):
        print("No")
        return

    # 2. Check if |S| = |T| = 26
    if len(S) == 26:
        print("Yes")
        return

    # 3. Check if S and T have the same set of characters
    if set(S) == set(T):
        print("Yes")
        return

    # 4. Check if S and T have the same number of distinct characters
    if len(set(S)) == len(set(T)):
        print("Yes")
        return

    print("No")
    return

main()
