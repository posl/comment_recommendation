Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
        return
    for i in range(1, len(S)):
        if S[i:] + S[:i] == T:
            print('Yes')
            return
    print('No')
    return

=======
Suggestion 2

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        for i in range(1, len(s)):
            if s[i:] + s[:i] == t:
                print("Yes")
                break
        else:
            print("No")

main()

=======
Suggestion 3

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(1, len(S)):
        if S == T[i:] + T[:i]:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 4

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        for i in range(1, len(s)):
            if (s[i:] + s[:i]) == t:
                print("Yes")
                break
        else:
            print("No")

=======
Suggestion 5

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        for i in range(1, 26):
            if S[-i:] + S[:-i] == T:
                print("Yes")
                return
        print("No")

=======
Suggestion 6

def main():
    s = input()
    t = input()
    n = len(s)
    for i in range(26):
        ans = True
        for j in range(n):
            if s[j] != t[(j+i)%n]:
                ans = False
                break
        if ans:
            print("Yes")
            return
    print("No")

=======
Suggestion 7

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(1, 26):
        S = ''.join([chr((ord(c) - ord('a') + i) % 26 + ord('a')) for c in S])
        if S == T:
            print("Yes")
            return
    print("No")

=======
Suggestion 8

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(1, 26):
        if "".join([chr((ord(x) - ord("a") + i) % 26 + ord("a")) for x in S]) == T:
            print("Yes")
            return
    print("No")

=======
Suggestion 9

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(1, 26):
        if ord(S[0]) + i > ord('z'):
            k = ord(S[0]) + i - ord('a')
        else:
            k = i
        if ord(T[0]) == ord(S[0]) + k:
            for j in range(1, len(S)):
                if ord(S[j]) + k > ord('z'):
                    k1 = ord(S[j]) + k - ord('a')
                else:
                    k1 = k
                if ord(T[j]) != ord(S[j]) + k1:
                    print("No")
                    return
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 10

def main():
    S = input()
    T = input()
    #print(S)
    #print(T)
    for i in range(len(S)):
        if ord(S[i]) - ord(T[i]) < 0:
            if ord(S[i]) - ord(T[i]) + 26 >= 0:
                continue
            else:
                print("No")
                return
        else:
            if ord(S[i]) - ord(T[i]) - 26 <= 0:
                continue
            else:
                print("No")
                return
    print("Yes")
    return
