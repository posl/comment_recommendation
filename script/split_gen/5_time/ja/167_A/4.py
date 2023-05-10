def is_ok(S, T):
    if len(S) + 1 != len(T):
        return False
    if S == T[:-1]:
        return True
    else:
        return False
S = input()
T = input()
print("Yes" if is_ok(S, T) else "No")
