def alphametic(s1, s2, s3):
    if len(s1) < len(s3):
        s1, s3 = s3, s1
    if len(s2) < len(s3):
        s2, s3 = s3, s2
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    if len(s1) < len(s3):
        s1, s3 = s3, s1
    if len(s2) < len(s3):
        s2, s3 = s3, s2
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    if len(s1) == len(s2) == len(s3):
        if len(s1) == 1:
            if s1 == s2 == s3:
                return '0', '0', '0'
            elif s1 == s2:
                return '1', '1', '2'
            elif s1 == s3:
                return '1', '2', '3'
            elif s2 == s3:
                return '2', '3', '5'
            else:
                return 'UNSOLVABLE'
        else:
            if s1[-1] == s2[-1] == s3[-1]:
                if s1[-1] == '0':
                    return 'UNSOLVABLE'
                else:
                    n1, n2, n3 = alphametic(s1[:-1], s2[:-1], s3[:-1])
                    if n1 == 'UNSOLVABLE':
                        return 'UNSOLVABLE'
                    else:
                        return n1 + '1', n2 + '1', n3 + '2'
            elif s1[-1] == s2[-1]:
                if s1[-1] == '0':
                    return 'UNSOLVABLE'
                else:
                    n1, n2, n3 = alphametic(s1[:-1], s2[:-1], s3[:-1])
                    if n1 == 'UNSOLVABLE':
                        return 'UNSOLVABLE'
                    else:
                        return n1 + '1', n2 + '1', n3 + '1'
            elif s1[-1] == s

if __name__ == '__main__':
    alphametic()