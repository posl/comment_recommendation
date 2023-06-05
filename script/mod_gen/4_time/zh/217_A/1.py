def judge(s,t):
    if len(s) < len(t):
        return "Yes"
    elif len(s) > len(t):
        return "No"
    else:
        for i in range(len(s)):
            if s[i] == t[i]:
                continue
            elif s[i] < t[i]:
                return "Yes"
            else:
                return "No"
        return "No"

if __name__ == '__main__':
    judge()