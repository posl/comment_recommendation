def is_multiple_8(s):
    if len(s) == 1:
        if int(s) % 8 == 0:
            return True
        else:
            return False
    elif len(s) == 2:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            return True
        else:
            return False
    else:
        if int(s) % 8 == 0:
            return True
        else:
            for i in range(len(s)):
                for j in range(i+1, len(s)):
                    for k in range(j+1, len(s)):
                        if int(s[i] + s[j] + s[k]) % 8 == 0:
                            return True
                        elif int(s[i] + s[k] + s[j]) % 8 == 0:
                            return True
                        elif int(s[j] + s[i] + s[k]) % 8 == 0:
                            return True
                        elif int(s[j] + s[k] + s[i]) % 8 == 0:
                            return True
                        elif int(s[k] + s[i] + s[j]) % 8 == 0:
                            return True
                        elif int(s[k] + s[j] + s[i]) % 8 == 0:
                            return True
            return False

if __name__ == '__main__':
    is_multiple_8()