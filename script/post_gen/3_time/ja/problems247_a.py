Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    s = list(s)
    for i in range(len(s)):
        if s[i] == "1":
            s[i] = "0"
        else:
            s[i] = "1"
    print("".join(s))

=======
Suggestion 2

def main():
    s = input()
    print(s[1:]+s[0])

=======
Suggestion 3

def main():
    S = input()
    print(S[1:]+S[0])

=======
Suggestion 4

def main():
    S = input()
    S_list = list(S)
    S_list.append("0")
    S_list.pop(0)
    print("".join(S_list))
