def check_string(s):
    t = s[:len(s)//2]
    if s == t + t:
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    check_string()