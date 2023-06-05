def is_wonderful(s):
    if len(s) < 2:
        return 'No'
    if len(s) == 2:
        if s[0].isupper() and s[1].islower():
            return 'Yes'
        else:
            return 'No'
    for i in range(len(s)):
        if s[i].isupper():
            for j in range(i+1,len(s)):
                if s[j].islower():
                    if s[i].lower() == s[j].lower():
                        return 'Yes'
                    else:
                        return 'No'
    return 'No'
