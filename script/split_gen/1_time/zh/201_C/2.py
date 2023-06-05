def f(S):
    S = S.replace('o','1')
    S = S.replace('x','0')
    S = S.replace('?','2')
    S = S.replace('2','?')
    return int(S,3)
S = input()
print(f(S))
