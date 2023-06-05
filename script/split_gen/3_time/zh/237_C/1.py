def check_palindromic(s):
    if len(s) == 1:
        return True
    else:
        for i in range(len(s)//2):
            if s[i] != s[-(i+1)]:
                return False
        return True
