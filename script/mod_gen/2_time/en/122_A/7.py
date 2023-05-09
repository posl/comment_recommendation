def get_bonded_base(base):
    if base == 'A':
        return 'T'
    elif base == 'T':
        return 'A'
    elif base == 'C':
        return 'G'
    elif base == 'G':
        return 'C'
    else:
        return 'Wrong Input'

if __name__ == '__main__':
    get_bonded_base()