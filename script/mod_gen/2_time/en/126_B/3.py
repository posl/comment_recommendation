def checkMMYY(s):
    if s[2:] == "00" or s[2:] == "01" or s[2:] == "02" or s[2:] == "03" or s[2:] == "04" or s[2:] == "05" or s[2:] == "06" or s[2:] == "07" or s[2:] == "08" or s[2:] == "09" or s[2:] == "10" or s[2:] == "11" or s[2:] == "12":
        return True
    else:
        return False

if __name__ == '__main__':
    checkMMYY()