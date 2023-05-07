def is_valid(n1,n2,n3):
    if len(n1) != len(n2) or len(n1) != len(n3) or len(n2) != len(n3):
        return False
    if n1[0] == '0' or n2[0] == '0' or n3[0] == '0':
        return False
    return True
