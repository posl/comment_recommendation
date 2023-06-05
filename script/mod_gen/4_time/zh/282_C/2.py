def replace(s):
    s = list(s)
    for i in range(len(s)):
        if i % 2 == 0:
            s[i] = "."
    return "".join(s)
 
N = int(input())
S = input()
print(replace(S))
