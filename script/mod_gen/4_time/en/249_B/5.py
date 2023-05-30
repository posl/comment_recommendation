def is_wonderful(s):
    return len(s) == len(set(s)) and s.lower() != s and s.upper() != s
s = input()
print("Yes" if is_wonderful(s) else "No")
