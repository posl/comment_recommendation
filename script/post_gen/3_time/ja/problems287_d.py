Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        if S[:i] + S[-len(T)+i:] == T:
            print("Yes")
        else:
            print("No")

=======
Suggestion 2

def main():
    s = input()
    t = input()
    for i in range(len(t)+1):
        if s[:i] + s[-(len(t)-i):] == t:
            print('Yes')
        else:
            print('No')

=======
Suggestion 3

def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        if S[:i]+S[-(len(T)-i):]==T:
            print("Yes")
        else:
            print("No")

=======
Suggestion 4

def main():
    s = input()
    t = input()
    for i in range(len(t)+1):
        s1 = s[:i]
        s2 = s[-(len(t)-i):]
        if s1+s2 == t:
            print("Yes")
        else:
            print("No")

main()

=======
Suggestion 5

def main():
    s = input()
    t = input()

    for i in range(len(t)+1):
        s1 = s[:i]
        s2 = s[len(s)-len(t)+i:]
        if s1+s2 == t:
            print("Yes")
        else:
            print("No")

=======
Suggestion 6

def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        if S[:i].find("?") == -1 and S[-(len(T)-i):].find("?") == -1:
            if S[:i]+S[-(len(T)-i):] == T:
                print("Yes")
            else:
                print("No")
        else:
            print("No")

=======
Suggestion 7

def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        S_prime = S[0:i] + S[-(len(T)-i):]
        flag = True
        for j in range(len(T)):
            if S_prime[j] == T[j] or S_prime[j] == "?" or T[j] == "?":
                continue
            else:
                flag = False
                break
        if flag:
            print("Yes")
        else:
            print("No")

=======
Suggestion 8

def main():
    S = input()
    T = input()
    N = len(S)
    M = len(T)
    for i in range(M+1):
        S_ = S[i:N-M+i]
        for j in range(M):
            if S_[j] == T[j] or S_[j] == "?" or T[j] == "?":
                if j == M-1:
                    print("Yes")
            else:
                print("No")
                break

=======
Suggestion 9

def main():
    # S = input()
    # T = input()
    S = 'beginner'
    T = 'contest'
    for i in range(len(T)+1):
        print('Yes' if T == S[i:i+len(T)] else 'No')
