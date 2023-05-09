def judge_repeat_string(s):
    if len(s) % 2 != 0:
        return False
    else:
        mid = len(s) // 2
        if s[:mid] == s[mid:]:
            return True
        else:
            return False
