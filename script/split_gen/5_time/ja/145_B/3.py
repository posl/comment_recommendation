def check(s):
    if len(s) % 2 == 1:
        return False
    else:
        half = len(s) // 2
        if s[:half] == s[half:]:
            return True
        else:
            return False
N = int(input())
S = input()
