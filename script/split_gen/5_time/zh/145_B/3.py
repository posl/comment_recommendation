def check(s):
    if len(s) % 2 != 0:
        return False
    else:
        half = len(s) // 2
        if s[:half] == s[half:]:
            return True
        else:
            return False
n = int(input())
s = input()
