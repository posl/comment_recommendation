def main():
    # read the data
    s = input()
    # process the data
    # YYMM format
    if 1 <= int(s[2:4]) <= 12:
        if 1 <= int(s[0:2]) <= 12:
            ans = 'AMBIGUOUS'
        else:
            ans = 'YYMM'
    else:
        if 1 <= int(s[0:2]) <= 12:
            ans = 'MMYY'
        else:
            ans = 'NA'
    # print the answer
    print(ans)
