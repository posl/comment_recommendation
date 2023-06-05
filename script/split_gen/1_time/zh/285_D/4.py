def judge(n, s, t):
    if n == 1:
        return 'Yes'
    else:
        for i in range(n):
            if s[i] == t[i]:
                return 'No'
        for i in range(n):
            for j in range(i+1, n):
                if s[i] == t[j] and s[j] == t[i]:
                    return 'Yes'
        return 'No'
