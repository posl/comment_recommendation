def shift(s, n):
    #convert string to list
    s = list(s)
    #convert each letter to its ascii code
    for i in range(len(s)):
        s[i] = ord(s[i])
    #add n to each ascii code
    for i in range(len(s)):
        s[i] = s[i] + n
    #convert each ascii code to its letter
    for i in range(len(s)):
        s[i] = chr(s[i])
    #convert list to string
    s = ''.join(s)
    return s
