def check_prefix(s,t):
    if s == t[0:len(s)]:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    check_prefix()