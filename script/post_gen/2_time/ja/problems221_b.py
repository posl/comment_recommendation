Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    T = input()

    count = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            count += 1

    if count == 2 or count == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(len(S)-1):
        if S[:i] + S[i+1] + S[i] + S[i+2:] == T:
            print("Yes")
            return
    print("No")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    l = len(s)
    cnt = 0
    for i in range(l):
        if s[i] != t[i]:
            cnt += 1
    if cnt == 0 or cnt == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(len(S) - 1):
        if S[i] == T[i + 1] and S[i + 1] == T[i]:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 5

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        for i in range(len(S) - 1):
            S = S[:i] + S[i + 1] + S[i] + S[i + 2:]
            if S == T:
                print("Yes")
                break
            S = S[:i] + S[i + 1] + S[i] + S[i + 2:]
        else:
            print("No")

=======
Suggestion 6

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            s_list = list(s)
            s_list[i], s_list[i+1] = s_list[i+1], s_list[i]
            s = "".join(s_list)
            break
    if s == t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(len(S)-1):
        if S[i] != T[i]:
            if S[i+1] != T[i+1]:
                if S[i] == T[i+1] and S[i+1] == T[i]:
                    print("Yes")
                    return
    print("No")
    return

=======
Suggestion 8

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        for i in range(len(S)):
            if S[i] != T[i]:
                if S[i+1:] == T[i+1:]:
                    print("Yes")
                    break
                else:
                    print("No")
                    break

=======
Suggestion 9

def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
    else:
        for i in range(len(S)):
            if S[i] != T[i]:
                tmp = S[i]
                S = S[:i] + S[i+1]
                S = S[:i+1] + tmp + S[i+1:]
                if S == T:
                    print('Yes')
                    break
                else:
                    print('No')
                    break

=======
Suggestion 10

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        exit()
    for i in range(0, len(S)-1):
        S = S[:i]+S[i+1]+S[i]+S[i+2:]
        if S == T:
            print("Yes")
            exit()
        S = S[:i]+S[i+1]+S[i]+S[i+2:]
    print("No")
    exit()
