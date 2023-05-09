def rotate(s):
    return s[1:] + s[0]
S = input()
T = input()
for _ in range(len(S)):
    if S == T:
        print("Yes")
        exit()
    S = rotate(S)
print("No")
