def get_result(s):
    if int(s[0:2]) > 12 and int(s[2:4]) > 12:
        return 'NA'
    elif int(s[0:2]) > 12 and int(s[2:4]) <= 12:
        return 'MMYY'
    elif int(s[0:2]) <= 12 and int(s[2:4]) > 12:
        return 'YYMM'
    else:
        return 'AMBIGUOUS'

if __name__ == '__main__':
    get_result()