Synthesizing 1/10 solutions

=======
Suggestion 1

def solve():
    s = input()
    if len(s) == 1:
        if s == "8":
            print("Yes")
        else:
            print("No")
        return
    if len(s) == 2:
        if s == "16" or s == "24" or s == "32" or s == "48" or s == "56" or s == "64" or s == "72" or s == "88" or s == "96":
            print("Yes")
        else:
            print("No")
        return
    i
