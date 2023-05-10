def check_str(s):
    #print(s)
    if s[0] in ['H','D','C','S'] and s[1] in ['A','2','3','4','5','6','7','8','9','T','J','Q','K']:
        return True
    else:
        return False
