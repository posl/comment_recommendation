Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    print(len(set(S)))

=======
Suggestion 2

def main():
    s = input()
    print(len(set(s)))

=======
Suggestion 3

def main():
    s = input()
    s_list = []
    for i in s:
        s_list.append(i)
    s_set = set(s_list)
    print(len(s_set))

=======
Suggestion 4

def main():
    S = input()
    S = list(S)
    S.sort()
    S = "".join(S)
    S = S.replace(" ", "")
    S = S.replace("\n", "")
    print(S)
    if S == "abc":
        print("Yes")
    else:
        print("No")
