def judge_strong_palindrome(s):
    if s == s[::-1]:
        s_len = len(s)
        if s[:(s_len-1)//2] == s[:(s_len-1)//2:-1] and s[(s_len+3)//2-1:] == s[(s_len+3)//2-1::-1]:
            return True
    return False
