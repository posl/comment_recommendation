def rotate(s):
    s = s[-1] + s[0:-1]
    return s
S = input()
T = input()
for i in range(len(S)):
    S = rotate(S)
    if S == T:
        print('Yes')
        break
else:
    print('No')
