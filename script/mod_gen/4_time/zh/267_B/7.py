def problem267_b(s):
    s0 = s[0]
    s1 = s[1]
    s2 = s[2]
    s3 = s[3]
    s4 = s[4]
    s5 = s[5]
    s6 = s[6]
    s7 = s[7]
    s8 = s[8]
    s9 = s[9]
    if s0 == '0':
        if s1 == '0':
            if s2 == '0':
                if s3 == '1':
                    if s4 == '1':
                        if s5 == '1':
                            if s6 == '0':
                                if s7 == '1':
                                    if s8 == '0':
                                        if s9 == '1':
                                            return 'Yes'
    return 'No'

if __name__ == '__main__':
    problem267_b()